#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${CURSOR_PLUGINS_LOCAL:-$HOME/.cursor/plugins/local}/ai-driven-workflow"

mkdir -p "$(dirname "$TARGET")"
ln -sfn "$ROOT" "$TARGET"

mkdir -p "$ROOT/.cursor/commands" "$ROOT/.cursor/skills" "$ROOT/.cursor/rules" "$ROOT/.cursor/agents"

for f in build-feature design fix-bug; do
  ln -f "$ROOT/commands/$f.md" "$ROOT/.cursor/commands/$f.md"
done

for d in "$ROOT/skills"/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  ln -sfn "$ROOT/skills/$name" "$ROOT/.cursor/skills/$name"
done

for f in "$ROOT/rules"/*.mdc; do
  [ -f "$f" ] || continue
  ln -f "$f" "$ROOT/.cursor/rules/$(basename "$f")"
done

# Cursor does not discover subagents that are symlinks under .cursor/agents; hard-link instead.
for f in "$ROOT/agents"/*.md; do
  [ -f "$f" ] || continue
  ln -f "$f" "$ROOT/.cursor/agents/$(basename "$f")"
done

ln -f "$ROOT/hooks/hooks.json" "$ROOT/.cursor/hooks.json"
ln -f "$ROOT/mcp.json" "$ROOT/.cursor/mcp.json"

echo "Linked: $TARGET -> $ROOT"
echo "Workspace mirrors under $ROOT/.cursor/ (hard links for files; skill dirs symlinked)"
echo "Restart Cursor (or Developer: Reload Window) to load the plugin."
