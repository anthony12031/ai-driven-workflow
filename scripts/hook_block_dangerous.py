import json
import re
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"permission": "allow"}))
        return
    cmd = data.get("command") or ""
    patterns = [
        r"rm\s+(-[rf]*\s+)+/",
        r"git\s+push\b.*--force",
        r"git\s+push\b.*\s-f\b",
        r"\bdrop\s+database\b",
        r"\btruncate\s+table\b",
    ]
    if any(re.search(p, cmd, re.IGNORECASE) for p in patterns):
        print(
            json.dumps(
                {
                    "permission": "deny",
                    "user_message": "This command was blocked by the ai-driven-workflow plugin.",
                    "agent_message": "Choose a safer alternative or ask the user to run the command manually.",
                }
            )
        )
    else:
        print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
