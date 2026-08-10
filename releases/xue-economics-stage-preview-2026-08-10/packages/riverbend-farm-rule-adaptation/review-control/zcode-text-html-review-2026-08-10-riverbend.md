I've read all 11 declared files. Now I'll cross-check hashes, narration consistency, HTML structure, and counts. This is a pure read-only review — no implementation to plan. Delivering the compact review in the requested format.

---

# Riverbend Farm Rule Adaptation — Bounded Text/HTML Review

## Findings

### [P2] Independent full-package review task identifiers reference "lesson_005", but this package is Lesson 004
- **Status**: Verified local
- **Location**: `final/story-manifest.yaml:51-52`; `final-checkpoint.yaml:36-37`
- **Scenario/impact**: Both independent full-package review records carry `reviewer_task: /root/review_validate_lesson_005` and `/root/validate_lesson_005`, while `story.yaml:9`, `story-manifest.yaml:6`, and `final-checkpoint.yaml:6` all declare `lesson_id: "004"` (and `series_order: 4`). If the task paths are literal script/automation identifiers, the reviews may have been run by a task wired to the wrong lesson; if they are merely mislabeled, the review provenance is misleading. Either way the text-level provenance chain names the wrong lesson for a Lesson 004 package.
- **Evidence chain**: `story.yaml:9 lesson:"004"` ≠ `story-manifest.yaml:51 reviewer_task:/root/review_validate_lesson_005` (same at :52, checkpoint :36-37). Review A/B hashes are three-way consistent across manifest/checkpoint/review-package, so the records exist and are bound — but their task labels don't match the lesson.
- **Falsifiable verification step**: Open `review-control/independent-final-review-a.yaml` and `-b.yaml` (not in the 11 declared files) and confirm each record's `story_id` is `riverbend-farm-rule-adaptation` and `lesson_id` is `004`, not `005`. If they reference lesson 005, the reviews covered the wrong basis and must be rerun.

### [P3] HTML exposes a visible `旁白` narrator label on all seven cards
- **Status**: Verified local (visible-text check)
- **Location**: `final/story.html:48,49,50,51,52,53,54` — each `<p class="narration"><strong>旁白</strong>…`
- **Scenario/impact**: Every card renders a visible "旁白" (narrator) strong-label before the narration text. This is a consistent project pattern (prior packages use it identically), and no card has dialogue (`text-layer.yaml` `dialogue: []` for all 7), so it is not confusing between speakers. But Q3 explicitly asks whether a visible `旁白` tag is exposed — it is. Whether the project intends a visible narrator label or plain narration text should be confirmed; if the latter, the `<strong>旁白</strong>` should be dropped.
- **Evidence chain**: `story.html:48` `<strong>旁白</strong>冯澜种菜…`; `text-layer.yaml:10 dialogue: []`.
- **Falsifiable verification step**: Confirm against the project's HTML style contract whether `旁白` is an intended visible label; if not, remove the `<strong>旁白</strong>` prefix and render narration as plain `.narration` text.

### [P3] Four basis-file hashes are declared only in the review prompt, not cross-referenced by any attached file
- **Status**: Inference
- **Location**: `storyboard.yaml`, `card-plan.yaml`, `visual-plan.yaml`, `continuity-ledger.yaml` — declared SHA-256 in the fixed basis list only
- **Scenario/impact**: `story-manifest.yaml` cross-references `story_sha256` and `text_layer_sha256` (verifiable), but no attached file references the hashes of `storyboard.yaml`, `card-plan.yaml`, `visual-plan.yaml`, or `continuity-ledger.yaml`. I read their content and confirmed internal consistency with the other files, but their declared hashes cannot be cross-verified from the 11 attached files alone.
- **Evidence chain**: `story-manifest.yaml:10-13` references story.yaml + text-layer.yaml only; checkpoint/review-package do not reference the four planning files' hashes.
- **Falsifiable verification step**: Run `shasum -a 256` on the four files and compare to the declared basis hashes (requires shell; not done in this read-only review).

## Rejected candidates

- **Card 4 "边缘地" vs visual-plan "低矮牧草的边缘菜畦"** — considered as a referent ambiguity. Rejected: the narration is intentionally general ("改种边缘地"); the visual-plan provides the precise asset contract. The two are compatible generalization↔specification, not contradiction. text-layer and HTML narration match verbatim.
- **excluded_history lists `card-005.png` and `card-001-candidate.png`** — considered as stale inclusion. Rejected: card 005's `source_path` is `card-005-r2.png` (manifest:32) and card 001's is `card-001-r2.png` (manifest:28); the excluded entries are the superseded originals, correctly retained locally but not in final/HTML. Consistent revision lineage.
- **HTML `lead`/`boundary`/`nav` text not present in `narration.md`** — considered as stale/extra text. Rejected: these are HTML framing elements (intro, boundary disclaimer, navigation), not card narration. They do not duplicate or contradict any of the seven frozen narrations.
- **Two independent reviews' YAML content not attached** — considered as an evidence gap rising to P2. Rejected as P2, kept as evidence gap: the review-record *hashes* are three-way consistent (manifest:51-52 = checkpoint:36-37 = review-package:15-16), and their *existence* is text-verifiable; only their *content* is unverified. The P2 reviewer_task mislabel already captures the provenance concern.

## Q1–Q5 answers

**Q1 (causal sequence / lifecycle distinction):** Yes — text-verified. Seven beats progress: intent (C1) → reciprocal harm (C2) → rule-changes-cost (C3, fence-line pilot begins) → participant adaptation (C4) → compare arrangements (C5) → baseline uncertainty (C6) → procedural close (C7). Time lineage is explicit in `continuity-ledger.yaml`: first_morning → same_morning → first_pilot_day → later_pilot_day → comparison_day → review_day. The fence-line arrangement lifecycle (candidate C1-2 → piloted C3-4 → compared C5-6) and buffer-strip lifecycle (candidate, not piloted, not observed, C2/5/6) are stated identically in `story.yaml:29-30`, `card-plan.yaml:24-25`, `visual-plan.yaml:24-25`, and `continuity-ledger.yaml:11-12`. The pilot/unpiloted distinction is consistent across all four sources. ✓ (visual confirmation Not verified)

**Q2 (narration agreement across six sources):** Yes — all seven narrations agree verbatim across `text-layer.yaml`, `final/narration.md`, and `final/story.html`; and semantically across `storyboard.yaml`, `card-plan.yaml` (via beats/coverage), `visual-plan.yaml` (via scenes), and `continuity-ledger.yaml` (via transfer_state/form). No omissions, contradictions, or cards un-understandable from the text contract. Exact-count keys in `visual-plan.yaml` match asset keys in `continuity-ledger.yaml` for all seven cards (cross-checked card-by-card). ✓

**Q3 (HTML visible labels / stale / duplicate / mismatch):** The visible `旁白` strong-label is present on all seven cards (P3 above). No stale text, no duplicate text, no mismatch with frozen narration — all seven HTML narration strings match `text-layer.yaml` and `narration.md` character-for-character. HTML card titles match `text-layer.yaml` titles for all seven. Alt texts are consistent with (not contradictory to) narrations. ✓ aside from the `旁白` label observation.

**Q4 (760px / 360px breakpoint source-level readability):** Yes — source-level readable. `@media (max-width:760px)` collapses `.card` from 2-column grid to 1-column (`grid-template-columns:1fr`), resets even-card visual order, switches images to `aspect-ratio:3/4`, and adjusts copy padding. `@media (max-width:360px)` narrows the container (`min(100% - 20px, 1120px)`) and shrinks nav padding. No fixed-width overflow risk visible at source level. Live rendering, font rasterization, and visual appearance: **Not verified.** ✓ (source-level)

**Q5 (counts / local refs / zero remote / formal=false / one-way hash):** All verified local. Seven cards: manifest cards list=7, HTML articles=7, `static_card_count:7`. Seven narrations: `narration_sections:7`, narration.md `## Card` headings=7, HTML `<p class="narration">`=7. Local image refs: HTML `src="cards/00N.png"` ×7, all local; `external_dependencies:0`, `remote_resource_count:0`. `formal:false` at manifest:55, checkpoint:45, review-package:3. One-way hash binding: checkpoint:17-19 (`final_checkpoint_binds_review_package_one_way`) and review-package:32 ("This file does not bind final-checkpoint.yaml") — consistent. Seven PNG hashes in manifest:28-34 match the fixed-basis declaration exactly. IR hash `d7c346fb…` is four-way consistent (story.yaml:12, manifest:9, checkpoint:8, review-package:8). ✓

## Verdict

**Accept with conditions** (text/HTML axis only)

The text and HTML basis is internally consistent: narrations agree across six sources, counts and hashes close, the causal sequence and fence-line/buffer-strip lifecycle distinction are coherent, HTML structure is source-readable at both breakpoints, and formal=false / one-way binding are correctly retained. The package is **not** formally accepted and **no edits are authorized**.

**Conditions**:
1. **Visual external review remains open** — the seven PNGs were not visually reviewed in this turn (no pixel input). `final-checkpoint.yaml:40-44` records ZCode as `completed_not_verified_no_pixel_input` and ChatGPT Review Control as `blocked_before_submit_browser_unavailable`. A pixel-capable Review Control provider must complete a frozen-basis visual review before formal can change.
2. **Reconcile the P2 reviewer_task "lesson_005" mislabel** — confirm the two independent review records actually cover `riverbend-farm-rule-adaptation` / Lesson 004, not Lesson 005.
3. **`formal_package_counted` must stay `false`** until conditions 1 and 2 close.
4. **Do not resend the completed ZCode visual turn** (per checkpoint:47 `next_action`).

## Evidence gaps

- **No pixels reviewed**: the seven PNG card images (`final/cards/001.png`–`007.png`) were not received as image input this round. All visual exact-count, same-kind-exclusion, character-continuity, composition, and 320px/2–3-second readability claims in `visual-plan.yaml`, `continuity-ledger.yaml`, and the two independent review records are **Not verified** by this review. The `continuity-ledger.yaml` self-checks (`adult_roster_matches_visual_exact_count: pass_local_assertion`, `positive_exact_keys_match_ledger_assets: pass_local_assertion`) are local assertions, not independent pixel verification.
- **No live mobile render reviewed**: the 760px/360px breakpoint check is source-level (CSS/markup) only; no browser rendering was performed.
- **Two independent review record contents not reviewed**: `independent-final-review-a.yaml` and `-b.yaml` are referenced by hash (three-way consistent) but are not among the 11 declared files; their visual PASS verdicts are unverified by this review.
- **Four planning-file hashes uncross-referenced**: `storyboard.yaml`, `card-plan.yaml`, `visual-plan.yaml`, `continuity-ledger.yaml` hashes are declared in the fixed basis but not referenced by any other attached file; content was read and found consistent, but hashes were not recomputed (no shell).
- **Lesson 004 IR file not reviewed**: `ir_sha256 d7c346fb…` is four-way consistent across attached files, but the IR file itself (`lessons/004/knowledge.yaml`) was not read; `validated` maturity and PR-01/PR-02/FW-01/AP-01 boundary claims are unverified beyond the four-way hash citation.

**Boundary遵守**: read-only; no files modified; no shell/tools used beyond reading the 11 declared files; no pixels interpreted; no prior-session package used as evidence; no paid lesson text quoted or reconstructed.
