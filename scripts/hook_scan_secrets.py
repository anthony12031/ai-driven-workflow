import json
import os
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
    path_raw = data.get("file_path") or ti.get("file_path") or ""
    path = path_raw.lower()
    content = data.get("content") or ti.get("content") or ""
    if not content and path_raw and os.path.isfile(path_raw):
        try:
            with open(path_raw, encoding="utf-8", errors="replace") as f:
                content = f.read()
        except OSError:
            content = ""
    if not content:
        emit_allow(data)
        return
    if any(x in path for x in (".example", "sample", "mock", "fixture")):
        emit_allow(data)
        return
    patterns = [
        r"BEGIN\s+(RSA\s+)?PRIVATE\s+KEY",
        r"BEGIN\s+OPENSSH\s+PRIVATE\s+KEY",
    ]
    if any(re.search(p, content, re.IGNORECASE) for p in patterns):
        msg = "Read blocked: content may contain a private key. Redact or use a secret store."
        emit_deny(data, msg, msg)
    else:
        emit_allow(data)


if __name__ == "__main__":
    main()
