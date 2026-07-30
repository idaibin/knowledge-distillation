#!/usr/bin/env python3
"""Run deterministic positive and negative checks for the v0.1 IR contract."""

from __future__ import annotations

import copy
import sys
import tempfile
from pathlib import Path

import yaml

from validate_ir import ValidationError, validate


ROOT = Path(__file__).resolve().parents[1]


def mutate(data: dict, name: str) -> None:
    if name == "dangling_source_ref":
        data["principles"][0]["evidence"][0]["source_ref"] = "missing-source"
    elif name == "level_4_without_executable":
        data["artifact"]["selected_level"] = "level_4"
        data.pop("executable", None)
    elif name == "non_contiguous_steps":
        data["frameworks"][0]["steps"][1]["id"] = 9
    else:
        raise ValueError(f"unknown mutation: {name}")


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

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    total = len(cases["positive"]) + len(cases["negative_mutations"])
    print(f"PASS: {total} basic IR evaluations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
