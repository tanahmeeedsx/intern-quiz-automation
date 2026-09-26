# 🎯 Internship Quiz Automation

An automation project for managing and processing internship quiz submissions using **Baserow, n8n, Mattermost, and Python**.

## 🚀 Overview

This project automates the flow of internship quiz submissions from data collection to team notification.

```text
Baserow Quiz Form
       ↓
Quiz Submission
       ↓
     n8n
       ↓
Validation & Data Mapping
       ↓
Mattermost Notification
```

## 🛠️ Tech Stack

* **Baserow** — Quiz forms and submission database
* **n8n** — Workflow automation
* **Mattermost** — Team notifications
* **Python** — Submission validation
* **Git & GitHub** — Version control and documentation

## ✨ Features

* Internship quiz form management
* Automated submission processing
* Data validation
* Field mapping and transformation
* Mattermost notifications
* Sample submission data
* Secure credential management

## 📂 Project Structure

```text
intern-quiz-automation/
├── docs/
│   ├── architecture.md
│   ├── baserow-setup.md
│   ├── n8n-workflow.md
│   └── mattermost-notification.md
├── examples/
│   └── sample-submission.json
├── screenshots/
├── scripts/
│   └── validate-submission.py
├── workflows/
│   └── n8n-workflow-example.json
├── .gitignore
├── LICENSE
└── README.md
```

## 🧪 Local Validation

Run the validation script with:

```bash
python3 scripts/validate-submission.py
```

Example output:

```text
✅ Submission is valid
```

## 🔐 Security

Credentials and sensitive information should never be committed to the repository.

Use secure credential management for:

* API tokens
* Passwords
* Webhook URLs
* SMTP credentials
* Environment variables

## 📚 Documentation

* [Architecture](docs/architecture.md)
* [Baserow Setup](docs/baserow-setup.md)
* [n8n Workflow](docs/n8n-workflow.md)
* [Mattermost Notifications](docs/mattermost-notification.md)

## 👨‍💻 Author

**Tanjim Ahmed**

GitHub: [@tanahmeeedsx](https://github.com/tanahmeeedsx)

---

⭐ A practical DevOps and workflow automation project.
