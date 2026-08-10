# ZCode independent final review: broken-window-unseen-cost

- provider: `ZCode 0.16.1 / text-only session`
- session_id: `sess_2dbb632e-fe9c-4669-aba4-0472c446ea99` (reused; no new session)
- round_id: `broken-window-unseen-cost-zcode-r1`
- terminal_status: `completed` (CLI exit `0`; projection `idle`)
- provider_verdict: `PASS(text-only)`
- local_status: `text identity reconciliation passed; visual axis Not verified; ChatGPT Review Control pending; not formal`

## Fixed attachment basis

- `review-control/final-review-package.md`: `c5970594d6d1422987868f1411573f4407c8c38f44154c2f6cbc38ced163b693`
- `final/story-manifest.yaml`: `92b9c80d4afd904689793454e2957f50b2519d9797eeddae513c1760340618e6`
- `final/story.html`: `e354c46236a28fbcdffd91eba7a552cf4130a0a4f4a2882fc17ec89ae6a65a2f`
- `review-control/independent-final-visual-review-r2.yaml`: `81f8d2ea8b3808ae9401174b74dfd05f2710205319cbc14fc439fcd72ef6fbf9`
- `final-checkpoint.yaml`: `63f81fd95843235fb8fc925e4138da65f317778537fdf676548a4007d68283cf`

## Operation ledger

- prompt_sha256: `800d614d253814c47c6e58d7933dd61b76eabf82f6b106a72abfa6cfe2eada3b`
- initial invocation: `failed-before-submit` because this CLI rejected `--max-turns`; no provider request was created.
- submit operation: one successful retry of the same logical operation after removing only that rejected option; never resent after acceptance.
- trace_id: `c14ea396-28b3-4cac-ac66-de0817bcfaba`
- turn_id: `turn_c708cf5a-b59e-4871-bc29-52c5a5f14ace`
- wait/capture: bounded polling of the same running process; one attributed completed response.
- provider tool_call_count: `0` (text attachments only; local tools disallowed).

## Attributed outcome and local reconciliation

ZCode found no P0/P1. It reported one non-blocking P2: the current r2 visual-review prose uses the name `Lin Lan` for Card005 while the attached HTML/manifest use role labels and do not contain that name. The attached `text-layer.yaml` was not sent, so ZCode could not determine whether the name is canonical.

### Local reconciliation of P2

Independent local reconciliation against the frozen basis closed this item as `pass_text_identity`: the canonical story role `店主` is `林岚`, its visual key is `lin_lan`, and Card005 describes the same action. `Lin Lan` is the pinyin rendering in the r2 prose; HTML intentionally uses the role label, while the manifest is not a character-name display surface. The initial P2 was therefore an attachment-insufficiency `Not verified`, not a current-basis mismatch. This reconciliation does not enlarge ZCode's text-only evidence and does not change the visual limitation below.

Its text-only answers accepted the attached HTML/package boundary: seven cards and seven narration sections form the visible-repair to unseen-alternatives sequence; expenditure is not stated as net benefit; Cards003–006 stay in counterfactual/inference territory; Card007 and the HTML do not make a current-law, empirical, automatic-policy, or final normative claim. Hash declarations and old-r1-superseded/current-r2 binding were textually consistent. `formal: false`, `formal_package_counted: false`, and pending ChatGPT Review Control were retained.

## Hard limitation

No PNG was attached. ZCode did **not** verify pixel-dependent object/person counts, background exclusions, character continuity, composition, card/thumbnail readability at 320px or 2–3 seconds, crop pixel equivalence, HTML/image render behavior, or whether alt text matches the images. These remain `Not verified` on the ZCode axis. The text-only PASS is not a visual approval and does not authorize formal acceptance.
