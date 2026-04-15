import json
import re
import sys

from hook_io import emit_allow, emit_deny, tool_input


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"permission": "allow"}))
        return
    ti = tool_input(data)
    cmd = (data.get("command") or ti.get("command") or "").strip()
    patterns = [
        r"rm\s+(-[rf]*\s+)+/",
        r"git\s+push\b.*--force",
        r"git\s+push\b.*\s-f\b",
        r"\bdrop\s+database\b",
        r"\btruncate\s+table\b",
    ]
    if any(re.search(p, cmd, re.IGNORECASE) for p in patterns):
        emit_deny(
            data,
            "This command was blocked by the ai-driven-workflow plugin.",
            "Choose a safer alternative or ask the user to run the command manually.",
        )
    else:
        emit_allow(data)


if __name__ == "__main__":
    main()
