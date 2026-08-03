#!/usr/bin/env python3
"""Run deterministic positive and negative checks for the v0.1 IR contract."""

from __future__ import annotations

import copy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

from validate_ir import ValidationError, validate


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "knowledge.schema.yaml"


def mutate(data: dict, name: str) -> None:
    if name == "dangling_source_ref":
        data["principles"][0]["evidence"][0]["source_ref"] = "missing-source"
    elif name == "missing_verification_status":
        data["principles"][0]["evidence"][0].pop("verification_status", None)
    elif name == "missing_licensed_publication_constraints":
        data["usage"].pop("publication_constraints", None)
    elif name == "level_4_without_executable":
        data["artifact"]["selected_level"] = "level_4"
        data.pop("executable", None)
    elif name == "skill_target_below_level_4":
        data["artifact"]["selected_level"] = "level_3"
        data["artifact"]["render_targets"] = ["skill"]
    elif name == "non_contiguous_steps":
        data["frameworks"][0]["steps"][1]["id"] = 9
    else:
        raise ValueError(f"unknown mutation: {name}")


def schema_rejects(path: Path) -> tuple[bool, str]:
    checker = shutil.which("check-jsonschema")
    if checker is None:
        return False, "check-jsonschema is required for cross-validator cases"
    result = subprocess.run(
        [checker, "--schemafile", str(SCHEMA), str(path)],
        check=False,
        capture_output=True,
        text=True,
    )
    return result.returncode != 0, result.stdout + result.stderr


def main() -> int:
    cases = yaml.safe_load((ROOT / "evals/basic/cases.yaml").read_text(encoding="utf-8"))
    failures: list[str] = []

    for case in cases["positive"]:
        path = ROOT / case["path"]
        try:
            data = validate(path)
        except Exception as exc:  # report all unexpected validation failures
            failures.append(f"{case['name']}: unexpected failure: {exc}")
            continue
        selected = data["artifact"]["selected_level"]
        if selected != case["expected_level"]:
            failures.append(
                f"{case['name']}: expected {case['expected_level']}, got {selected}"
            )

    for case in cases["negative_mutations"]:
        base = yaml.safe_load((ROOT / case["base"]).read_text(encoding="utf-8"))
        data = copy.deepcopy(base)
        mutate(data, case["mutation"])
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", encoding="utf-8") as handle:
            yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True)
            handle.flush()
            try:
                validate(Path(handle.name))
            except ValidationError as exc:
                if case["expected_error"] not in str(exc):
                    failures.append(
                        f"{case['name']}: expected error containing "
                        f"{case['expected_error']!r}, got {str(exc)!r}"
                    )
            else:
                failures.append(f"{case['name']}: invalid mutation passed validation")
            if case.get("cross_validator") == "check-jsonschema":
                rejected, detail = schema_rejects(Path(handle.name))
                if not rejected:
                    failures.append(f"{case['name']}: check-jsonschema accepted invalid mutation: {detail}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    total = len(cases["positive"]) + len(cases["negative_mutations"])
    print(f"PASS: {total} basic IR evaluations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
