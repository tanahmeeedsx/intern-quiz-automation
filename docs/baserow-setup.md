# Baserow Setup

## Purpose

Baserow is used to create internship quiz forms and store submitted responses.

## Submission Fields

The automation uses the following fields:

- Participant
- Quiz Name
- Score
- Submitted At

## Data Flow

1. Participant submits the quiz form.
2. Baserow creates a new submission record.
3. The new record triggers the automation workflow.
4. n8n processes the submission.
5. The submission can be sent to Mattermost for team notification.

> Never store API tokens, passwords, or other credentials in this repository.
