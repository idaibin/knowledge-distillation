I have all 11 declared files plus both review records. Both findings can now be verified against the current fixed basis. This is a pure read-only reconciliation report — no implementation to plan.

---

# Riverbend Round2 Reconciliation — Both Attributed Findings

## Finding 1 (lifecycle uniformity + C3/C4/C6 visible transitions): **closed**

**Evidence paths:**

*Lifecycle block uniformity* — all six planning files carry an identical `lifecycle` block (c1_incident → c2_two_candidates_first_appear → c3_continuous_fence_first_short_term_pilot_day → c4_days_later_continue_short_term_pilot → c5_two_candidate_comparison → c6_baseline_if_no_trial_original_low_boundary → c7_procedural_close), plus a unified `arrangement_lifecycle` with a new `baseline` key (`c6_if_no_trial_continuous_fence_not_used_original_low_boundary_retained`):
- `story.yaml:17-28`
- `text-layer.yaml:6-17`
- `storyboard.yaml:4-15`
- `card-plan.yaml:4-15`
- `visual-plan.yaml:4-15`
- `continuity-ledger.yaml:5-21`

All six are byte-identical in their lifecycle keys. Version bumped to `0.3-lifecycle-reconciled` across all six.

*C3/C4/C6 visible copy states transitions* — the three required cards now carry explicit transition language in **all three visible-text sources** (text-layer.yaml, narration.md, story.html), verbatim-matched:
- **C3** (`text-layer.yaml:29`, `narration.md:13`, `story.html:50`): "两种候选安排刚摆出，今天先把连续栅栏作为首个短期试行" — states first-pilot-day transition. ✓
- **C4** (`text-layer.yaml:33`, `narration.md:17`, `story.html:51`): "数日后连续栅栏仍在短期试行；顾原继续改走石质草坡，冯澜继续把边缘菜畦改种低矮牧草" — states days-later continued-pilot + adaptation. ✓
- **C6** (`text-layer.yaml:41`, `narration.md:25`, `story.html:53`): "若不试行连续栅栏，原低边界会继续保留；把这条基线与短期试行的栅栏并列比较" — states no-trial→original-low-boundary baseline. ✓

*C1/C2/C5/C7* also carry their lifecycle-appropriate text (C1 incident, C2 two candidates first appear, C5 two-candidate comparison, C7 procedural close). All 7 HTML narration strings match text-layer.yaml and narration.md exactly. The `delete_card_test` (story.yaml:53-55) still passes.

**Residual risk:** Visual depiction of these transitions (e.g. Card03 actually showing "first pilot day" vs Card04 "days later") is **Not verified** — no pixels reviewed. The text contract is uniform; whether the frozen PNG bytes depict the transitions is a separate axis.

## Finding 2 (A/B reviews marked historical, current total 0/2): **closed**

**Evidence paths:**

*Current full-package count = 0/2:*
- `story-manifest.yaml:55-57`: `required: 2`, `completed: 0`, `historical_pre_html_fix_records_retained: true`
- `final-checkpoint.yaml:32-35`: `required: 2`, `completed: 0`, `historical_pre_html_fix_records_retained: true`
- `review-control/final-review-package.md:1`: "CURRENT FULL-PACKAGE REVIEWS 0/2"

*Both A/B records marked historical, not counting:*
- `story-manifest.yaml:60-61`: both records `decision: historical_pre_html_fix, counts_as_current_review: false`
- `final-checkpoint.yaml:37-38`: same
- `review-control/final-review-package.md:15-16,24`: both marked `historical_pre_html_fix, current count false`; "do not count toward the current full-package total, which is 0/2"

*A/B records preserved immutable:*
- `independent-final-review-a.yaml` and `-b.yaml` internals are **unchanged**: `decision: pass`, `effect: counts_as_one_of_two_required_independent_full_package_reviews`, `reviewed_snapshot.story_html sha256: 48994f6d...` (old HTML). The records were not rewritten — the current-count correction lives in the manifest/checkpoint/review-package *references*, not in the records themselves. ✓

*lesson_005 provenance gap retained:*
- `review-a.yaml:4` `reviewer_task: /root/review_validate_lesson_005`; `review-b.yaml:4` `/root/validate_lesson_005` — unchanged.
- `review-control/final-review-package.md:41`: "retained as provenance; they do not prove Lesson 004 coverage and were not rewritten. This remains a provenance gap, not a new story/HTML defect." ✓

**Residual risk:** A reader who opens `review-a.yaml` or `-b.yaml` in isolation still sees `decision: pass` and `effect: counts_as_one_of_two_required` — these internal fields were correctly left immutable per the peer's instruction, so the "does not count" correction is only visible via the manifest/checkpoint/review-package wrappers. This is an inherent tension of the immutability requirement, not a defect. The `/root/*lesson_005` provenance gap is retained as required but means the two historical reviews' actual lesson coverage remains unconfirmed.

## Additional observations (not among the two attributed findings)

- **HTML `旁白` label removed**: `story.html:48-54` no longer carries `<strong>旁白</strong>`; narration is now plain `<p class="narration">`. This closes the r1 P3 I raised. Not one of the two attributed findings, but a residual improvement. Seven narration strings still match text-layer/narration.md exactly.
- **All six planning-file hashes now cross-referenced**: `story-manifest.yaml:11-21` now references story/text-layer/storyboard/card-plan/visual-plan/continuity-ledger hashes. This closes my r1 P3 about uncross-referenced planning hashes. (Hash values match the fixed-basis declarations; recomputation not done — no shell.)
- **formal = false** retained at manifest:64, checkpoint:49-50, review-package:3. ✓
- **One-way hash binding** retained: checkpoint:17-19 binds review-package one-way; review-package:32 does not bind checkpoint. ✓
- **Seven PNG hashes unchanged** from round1 (manifest:36-42). ✓
- **Zero remote resources**, 7 cards / 7 narrations throughout. ✓

## Not verified (this round)

- **No pixels reviewed** — seven PNG bytes are frozen invariants only; visual exact-counts, same-kind exclusions, character continuity, composition, and 320px/2–3s readability all **Not verified**.
- **No live mobile render** — 760px/360px breakpoints checked at CSS source level only (`story.html:34-35`); `live_mobile_render: Not reverified` (checkpoint:30).
- **SHA-256 recomputation not performed** — read-only review, no shell; hash values cross-checked internally across files but not cryptographically recomputed.
- **Lesson 004 IR file not reviewed** — `ir_sha256 d7c346fb…` four-way consistent across attached files; IR content/validated-maturity unverified.
- **Two historical review records' visual PASS verdicts** — immutable records preserved but their visual claims (exact-counts, continuity, 320px readability) are **Not verified** by this round and do not count toward current total.

## Overall verdict: **Accept**

Both attributed findings are **closed** on the text/HTML axis:
1. Lifecycle is uniform across all six planning files, with C3/C4/C6 visible copy (HTML + narration.md + text-layer.yaml) stating the required transitions.
2. A/B reviews are preserved immutable, marked `historical_pre_html_fix` / `counts_as_current_review: false`, current completed total = 0/2, and the `lesson_005` provenance gap is explicitly retained.

This Accept is **text/HTML reconciliation only** — it does not authorize formal acceptance. `formal` remains `false`; a pixel-capable external Review Control round and current 0/2 → 2/2 full-package reviews are still required before formal can change. No visual approval is inferred.
