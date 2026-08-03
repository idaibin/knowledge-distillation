#!/usr/bin/env python3
"""Validate Knowledge Distillation IR v0.1 without network dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml


LEVELS = {"level_1", "level_2", "level_3", "level_4"}
RENDER_TARGETS = {"card", "model", "framework", "skill"}
MATURITY = {"draft", "reviewed", "validated", "executable"}
EVIDENCE_TYPES = {"citation", "experience", "observation", "inference"}
SOURCE_ACCESS = {"public", "private", "licensed", "internal", "unknown"}
VERIFICATION_STATUSES = {"source_supported", "independently_verified", "unverified"}
PUBLICATION_CONSTRAINTS = {
    "no_source_text", "no_source_substitute_positioning",
    "review_cumulative_coverage", "transform_source_specific_titles"
}


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def non_empty_list(value: Any, path: str) -> list[Any]:
    require(isinstance(value, list) and len(value) > 0, f"{path} must be a non-empty list")
    return value


def validate_evidence(items: Any, source_ids: set[str], path: str) -> None:
    for index, item in enumerate(non_empty_list(items, path)):
        current = f"{path}[{index}]"
        require(isinstance(item, dict), f"{current} must be an object")
        require(item.get("type") in EVIDENCE_TYPES, f"{current}.type is invalid")
        require(item.get("verification_status") in VERIFICATION_STATUSES,
                f"{current}.verification_status is invalid")
        require(item.get("source_ref") in source_ids, f"{current}.source_ref is not declared")
        require(bool(item.get("locator")), f"{current}.locator is required")


def validate(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict), "document root must be an object")

    required = {
        "metadata", "status", "sources", "usage", "boundary", "principles", "frameworks",
        "anti_patterns", "open_questions", "artifact"
    }
    missing = sorted(required - data.keys())
    require(not missing, f"missing top-level fields: {', '.join(missing)}")

    metadata = data["metadata"]
    require(isinstance(metadata, dict), "metadata must be an object")
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(metadata.get("id", ""))) is not None,
            "metadata.id must be lowercase hyphen-case")
    require(metadata.get("ir_version") == "0.1", "metadata.ir_version must be '0.1'")
    require(bool(metadata.get("title")) and bool(metadata.get("domain")) and bool(metadata.get("created_at")),
            "metadata.title, domain, and created_at are required")

    status = data["status"]
    require(isinstance(status, dict) and status.get("maturity") in MATURITY,
            "status.maturity is invalid")

    sources = non_empty_list(data["sources"], "sources")
    source_ids: set[str] = set()
    for index, source in enumerate(sources):
        require(isinstance(source, dict), f"sources[{index}] must be an object")
        source_id = source.get("id")
        require(isinstance(source_id, str) and source_id, f"sources[{index}].id is required")
        require(source_id not in source_ids, f"duplicate source id: {source_id}")
        require(bool(source.get("type")) and bool(source.get("reference")),
                f"sources[{index}].type and reference are required")
        require(source.get("access") in SOURCE_ACCESS,
                f"sources[{index}].access is required and must be valid")
        source_ids.add(source_id)

    usage = data["usage"]
    require(isinstance(usage, dict), "usage must be an object")
    require(usage.get("purpose") in {"personal_learning", "internal_training", "product_development", "public_content", "other"},
            "usage.purpose is invalid")
    require(usage.get("visibility") in {"private", "internal", "public"},
            "usage.visibility is invalid")
    require(usage.get("source_retention") in {"none", "locators_only", "transformed_notes", "full_source"},
            "usage.source_retention is invalid")
    require(usage.get("publication_review") in {"not_required", "required", "blocked"},
            "usage.publication_review is invalid")
    constraints = usage.get("publication_constraints", [])
    require(isinstance(constraints, list), "usage.publication_constraints must be a list")
    require(set(constraints) <= PUBLICATION_CONSTRAINTS,
            "usage.publication_constraints contains an invalid value")
    require(len(constraints) == len(set(constraints)),
            "usage.publication_constraints must be unique")
    restricted_source = any(source.get("access") in {"licensed", "private", "internal", "unknown"} for source in sources)
    if restricted_source:
        required_constraints = {"no_source_text", "no_source_substitute_positioning"}
        require(required_constraints <= set(constraints),
                "licensed/private/internal sources require publication safety constraints")
    serialized_restricted_source = any(
        source.get("access") in {"licensed", "unknown"}
        or (
            source.get("access") in {"private", "internal"}
            and source.get("type") in {"book", "course", "transcript"}
        )
        for source in sources
    )
    if serialized_restricted_source:
        require("review_cumulative_coverage" in constraints,
                "licensed or private serialized sources require cumulative coverage review")

    boundary = data["boundary"]
    require(isinstance(boundary, dict), "boundary must be an object")
    non_empty_list(boundary.get("include"), "boundary.include")
    non_empty_list(boundary.get("exclude"), "boundary.exclude")

    for section in ("principles", "frameworks", "anti_patterns"):
        require(isinstance(data[section], list), f"{section} must be a list")
        for index, item in enumerate(data[section]):
            require(isinstance(item, dict), f"{section}[{index}] must be an object")
            validate_evidence(item.get("evidence"), source_ids, f"{section}[{index}].evidence")

    for index, framework in enumerate(data["frameworks"]):
        steps = non_empty_list(framework.get("steps"), f"frameworks[{index}].steps")
        expected_ids = list(range(1, len(steps) + 1))
        actual_ids = [step.get("id") if isinstance(step, dict) else None for step in steps]
        require(actual_ids == expected_ids, f"frameworks[{index}].steps ids must be contiguous from 1")
        for step_index, step in enumerate(steps):
            require(bool(step.get("action")) and bool(step.get("check")),
                    f"frameworks[{index}].steps[{step_index}] needs action and check")
        non_empty_list(framework.get("boundaries"), f"frameworks[{index}].boundaries")

    require(isinstance(data["open_questions"], list), "open_questions must be a list")

    artifact = data["artifact"]
    require(isinstance(artifact, dict), "artifact must be an object")
    require(artifact.get("requested_level") in LEVELS | {"auto"}, "artifact.requested_level is invalid")
    selected = artifact.get("selected_level")
    require(selected in LEVELS, "artifact.selected_level is invalid")
    require(bool(artifact.get("rationale")), "artifact.rationale is required")
    render_targets = non_empty_list(artifact.get("render_targets"), "artifact.render_targets")
    require(set(render_targets) <= RENDER_TARGETS, "artifact.render_targets contains an invalid target")
    require(len(render_targets) == len(set(render_targets)), "artifact.render_targets must be unique")
    require(selected == "level_4" or "skill" not in render_targets,
            "skill render target requires selected_level level_4")

    executable = data.get("executable")
    if selected == "level_4" or status.get("maturity") == "executable":
        require(isinstance(executable, dict), "level_4 requires executable")
        for field in ("trigger", "inputs", "workflow", "outputs", "constraints", "validation"):
            require(field in executable, f"executable.{field} is required")
        non_empty_list(executable["trigger"].get("when"), "executable.trigger.when")
        non_empty_list(executable["trigger"].get("do_not_trigger_when"),
                       "executable.trigger.do_not_trigger_when")
        non_empty_list(executable["inputs"].get("required"), "executable.inputs.required")
        non_empty_list(executable["workflow"].get("steps"), "executable.workflow.steps")
        non_empty_list(executable.get("constraints"), "executable.constraints")
        tests = non_empty_list(executable["validation"].get("tests"), "executable.validation.tests")
        for index, test in enumerate(tests):
            require(isinstance(test, dict), f"executable.validation.tests[{index}] must be an object")
            require(bool(test.get("name")) and bool(test.get("input")),
                    f"executable.validation.tests[{index}] needs name and input")
            non_empty_list(test.get("expected_behavior"),
                           f"executable.validation.tests[{index}].expected_behavior")

    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ir", type=Path, help="Knowledge IR YAML file")
    args = parser.parse_args()
    try:
        data = validate(args.ir)
    except (OSError, yaml.YAMLError, ValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(
        f"VALID: {args.ir} | id={data['metadata']['id']} | "
        f"level={data['artifact']['selected_level']} | maturity={data['status']['maturity']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
