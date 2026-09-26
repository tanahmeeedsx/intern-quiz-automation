# n8n Workflow

## Purpose

n8n connects Baserow with the notification system and automates quiz submission processing.

## Workflow

1. Detect a new Baserow submission.
2. Receive the submission data.
3. Map the required fields.
4. Process the submission.
5. Send a notification to Mattermost.

## Fields

- Participant
- Quiz Name
- Score
- Submitted At

## Security

Credentials should be stored securely using n8n credentials or environment variables.

Do not commit credentials or access tokens to GitHub.
