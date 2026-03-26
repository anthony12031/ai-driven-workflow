#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then
  exec python3 "$ROOT/hook_block_dangerous.py"
fi
cat >/dev/null
echo '{"permission":"allow"}'
