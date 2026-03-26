import json
import os
import shutil
import subprocess
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        return
    path = data.get("file_path") or ""
    if not path or not os.path.isfile(path):
        return
    ext = os.path.splitext(path)[1].lower()
    cwd = os.path.dirname(path) or "."

    def run(cmd) -> None:
        try:
            subprocess.run(cmd, cwd=cwd, check=False, timeout=120)
        except Exception:
            pass

    if ext in (".ts", ".tsx", ".js", ".jsx", ".json", ".md", ".css", ".scss") and shutil.which("npx"):
        run(["npx", "--yes", "prettier", "--write", path])
    elif ext == ".py":
        if shutil.which("ruff"):
            run(["ruff", "format", path])
        elif shutil.which("black"):
            run(["black", "-q", path])
    elif ext == ".go" and shutil.which("gofmt"):
        run(["gofmt", "-w", path])
    elif ext == ".rs" and shutil.which("rustfmt"):
        run(["rustfmt", path])


if __name__ == "__main__":
    main()
