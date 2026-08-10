# ChatGPT Review Control preflight: riverbend-farm-rule-adaptation

- checked_at: `2026-08-10`
- provider: `ChatGPT Review Control`
- project_id: `g-p-6a7052bb5bf88191900a8a0c869c5291`
- route_priority: `Codex in-app browser`, then authorized local-browser fallback
- result: `blocked_before_submit`
- message_submitted: `false`
- attachment_uploaded: `false`
- conversation_created: `false`
- formal: `false`

## Verified before the blocker

The in-app browser opened the exact project URL and rendered the unique `Review Control` project identity, a Personal account category, one empty project composer, and one visible upload control. No existing review conversation was reused and no unrelated tab was inspected.

## Blocker

The first and only attachment attempt targeted the hidden file input while waiting for the browser file-chooser event. The chooser event timed out before any file path was passed to `setFiles`, so the contact sheet was not transmitted and the composer was not submitted. The browser control connection then reset. A fresh capability check returned no available in-app browser, and the explicitly permitted local Chrome fallback was also unavailable from the browser runtime.

Because there was no attachment side effect and no submit, this is a clean pre-submit blocker rather than an ambiguous external operation. The same attachment operation must not be retried until a fresh browser capability snapshot proves an exact Review Control project, a clean composer, and a working file chooser. No message, conversation, assistant response, verdict, or formal evidence exists for this intended round.

## Recovery boundary

Resume with the same fixed package only after the built-in browser or the authorized local browser exposes a controllable file chooser. Use a new browser operation attempt for the existing attachment operation ID; never infer a Review Control verdict from the local 2/2 reviews or from ZCode, and never mark `formal=true` before a captured provider response is locally reconciled.

