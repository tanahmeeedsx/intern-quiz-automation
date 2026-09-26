# Automation Architecture

## Workflow

Baserow Quiz Form
        ↓
Baserow Quiz Submissions
        ↓
n8n Automation
        ↓
Data Validation & Mapping
        ↓
Mattermost Notification

## Components

### Baserow
Used for creating quiz forms and storing participant submissions.

### n8n
Handles workflow automation, data processing, field mapping, and notifications.

### Mattermost
Used to notify the team when a new quiz submission is received.

### Python
A small validation script is included for testing submission data locally.
