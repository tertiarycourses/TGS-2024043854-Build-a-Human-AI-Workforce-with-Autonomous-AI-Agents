# One approved training email — separate from read-only gog-office

This procedure is used only for Activity 4's one test send. The read-only gog-office skill remains unchanged. Use an assigned Google training account and a trainer-approved test recipient; do not use customer or personal recipients.

1. Inspect `gog auth list --json` privately and `gog auth add --help`, `gog gmail send --help`. Do not print tokens or client JSON. Preserve the account's existing OAuth client, services, scope modes and extra grants when reauthorizing; Calendar/Drive must remain available.
2. Trainer preflights the installed Gmail write-scope mode needed for one send **and** Sent readback. A send-only grant may not allow reading Sent. Complete any changed consent in the provider browser, not chat. Do not broaden services because a read failed.
3. Save exact approved recipient, subject, body and attachment list locally. Start with no attachments. Show them to the human and wait for explicit SEND approval of that exact version. The email may not authorise its own send.
4. Preview with installed `--dry-run`. Only after exact approval, run the approved send once without runtime `--readonly` / `--gmail-no-send` on that one command. If account/global no-send policy still blocks it, the trainer resolves the authorised training policy or marks it blocked; never bypass another account's controls.

macOS/Bash reference (replace variables privately; inspect installed help):

```bash
gog --account "$GOG_ACCOUNT" gmail send --to "$TRAINING_RECIPIENT" --subject "Training launch update" --body-file outputs/lab02/approved-email.txt --dry-run
# Only after explicit human SEND approval of the exact preview:
gog --account "$GOG_ACCOUNT" --json gmail send --to "$TRAINING_RECIPIENT" --subject "Training launch update" --body-file outputs/lab02/approved-email.txt
# Replace ACTUAL_MESSAGE_ID with the real returned ID:
gog --account "$GOG_ACCOUNT" --readonly --gmail-no-send --json gmail get ACTUAL_MESSAGE_ID
```
PowerShell uses `$env:GOG_ACCOUNT` and `$env:TRAINING_RECIPIENT` instead of Bash variables. Browser consent and the native Desktop runtime must use the same assigned account/keyring.

5. Verify the actual returned message ID, Sent label and To/Subject/body against the approved version. Record one real send/readback in outputs/lab02/test-send-log.md. Do not auto-retry an uncertain send: check Sent first to avoid duplicates.
6. Resume the default read-only/no-send runtime flags on all further reads. No calendar changes, public sharing or follow-up automations are authorised.

If recipient, scope, approval or readback is unavailable, mark the send INCOMPLETE/BLOCKED and preserve the draft. A draft or tool success sentence is not proof of sending.

Official source checked 29 October 2026: https://gogcli.sh/gmail-workflows.html and https://gogcli.sh/quickstart.html
