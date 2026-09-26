import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "participant",
    "quiz_name",
    "score",
    "submitted_at",
]


def validate_submission(file_path):
    data = json.loads(Path(file_path).read_text())

    missing = [field for field in REQUIRED_FIELDS if field not in data]

    if missing:
        print(f"❌ Missing fields: {', '.join(missing)}")
        return False

    if not data["participant"]:
        print("❌ Participant cannot be empty")
        return False

    if not isinstance(data["score"], (int, float)):
        print("❌ Score must be a number")
        return False

    if data["score"] < 0:
        print("❌ Score cannot be negative")
        return False

    print("✅ Submission is valid")
    return True


if __name__ == "__main__":
    file = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "examples/sample-submission.json"
    )

    if not validate_submission(file):
        sys.exit(1)
