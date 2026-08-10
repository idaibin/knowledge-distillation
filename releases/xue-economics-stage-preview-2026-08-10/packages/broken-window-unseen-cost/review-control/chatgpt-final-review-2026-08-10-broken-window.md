# ChatGPT Review Control preflight: broken-window-unseen-cost

- checked_at: `2026-08-10 Asia/Shanghai`
- provider: `ChatGPT Review Control`
- intended_round_id: `broken-window-unseen-cost-chatgpt-r1`
- preflight_result: `blocked_before_target_or_conversation_inspection`
- formal: `false`

## Blocking evidence

The macOS UI bridge returned: `The Mac is locked and automatic unlock could not unlock it. Ask the user to unlock the Mac manually before continuing.`

This was a read-only lock-state check. No ChatGPT project, conversation, composer, model/reasoning selector, or file chooser was opened or inspected. No attachment was uploaded, no conversation was created, and no message was submitted; therefore no submit, capture, conversation URL, or turn identifier exists for this intended round.

## Frozen intended attachment set

The following current-basis files remain unchanged and unsent:

- `final-review-package.md`
- `../final/story-manifest.yaml`
- `../final/story.html`
- `independent-final-visual-review-r2.yaml`
- `../final-checkpoint.yaml`
- seven optional PNGs under `../final/cards/001.png` through `007.png`

## Resume rule

Resume only after a fresh read-only lock-state check proves the Mac is unlocked. Then re-freeze attachment SHA-256 values and verify the exact Review Control project, a single clean composer, model, and reasoning before one submit. Do not infer a verdict from ZCode or local reviews, and do not change `formal: false` or `formal_package_counted: false` until a captured ChatGPT finding is locally reconciled.
