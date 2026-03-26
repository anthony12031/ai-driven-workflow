import json
import re
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({"permission": "allow"}))
        return
    content = data.get("content") or ""
    path = (data.get("file_path") or "").lower()
    if not content:
        print(json.dumps({"permission": "allow"}))
        return
    if any(x in path for x in (".example", "sample", "mock", "fixture")):
        print(json.dumps({"permission": "allow"}))
        return
    patterns = [
        r"BEGIN\s+(RSA\s+)?PRIVATE\s+KEY",
        r"BEGIN\s+OPENSSH\s+PRIVATE\s+KEY",
    ]
    if any(re.search(p, content, re.IGNORECASE) for p in patterns):
        print(
            json.dumps(
                {
                    "permission": "deny",
                    "user_message": "Read blocked: content may contain a private key. Redact or use a secret store.",
                }
            )
        )
    else:
        print(json.dumps({"permission": "allow"}))


if __name__ == "__main__":
    main()
