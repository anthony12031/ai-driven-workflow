#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="${CURSOR_PLUGINS_LOCAL:-$HOME/.cursor/plugins/local}/ai-driven-workflow"
USER_CURSOR="${HOME}/.cursor"

same_inode() {
  local a="$1" b="$2"
  [[ -e "$a" && -e "$b" ]] || return 1
  local ia ib
  ia="$(stat -f %i "$a" 2>/dev/null || stat -c %i "$a" 2>/dev/null)" || return 1
  ib="$(stat -f %i "$b" 2>/dev/null || stat -c %i "$b" 2>/dev/null)" || return 1
  [[ "$ia" == "$ib" ]]
}

remove_skill_symlink_if_ours() {
  local dest="$1" name="$2"
  local expected="$ROOT/skills/$name"
  [[ -L "$dest" ]] || return 0
  local t
  t="$(readlink "$dest")"
  if [[ "$t" == "$expected" ]]; then
    rm -f "$dest"
  fi
}

dir_empty() {
  local d="$1"
  [[ -d "$d" ]] || return 1
  ! ls -A "$d" 2>/dev/null | grep -q .
}

echo "Removing ai-driven-workflow plugin registration: $TARGET"
if [[ -L "$TARGET" ]] || [[ -e "$TARGET" ]]; then
  rm -f "$TARGET"
fi

echo "Removing workspace mirrors under $ROOT/.cursor/"
for f in build-feature design fix-bug init-repo; do
  if [[ -f "$ROOT/.cursor/commands/$f.md" ]] && same_inode "$ROOT/.cursor/commands/$f.md" "$ROOT/commands/$f.md"; then
    rm -f "$ROOT/.cursor/commands/$f.md"
  fi
done

for f in "$ROOT/agents"/*.md; do
  [[ -f "$f" ]] || continue
  b="$(basename "$f")"
  if [[ -f "$ROOT/.cursor/agents/$b" ]] && same_inode "$ROOT/.cursor/agents/$b" "$f"; then
    rm -f "$ROOT/.cursor/agents/$b"
  fi
done

for f in "$ROOT/rules"/*.mdc; do
  [[ -f "$f" ]] || continue
  b="$(basename "$f")"
  if [[ -f "$ROOT/.cursor/rules/$b" ]] && same_inode "$ROOT/.cursor/rules/$b" "$f"; then
    rm -f "$ROOT/.cursor/rules/$b"
  fi
done

for d in "$ROOT/skills"/*/; do
  [[ -d "$d" ]] || continue
  name="$(basename "$d")"
  remove_skill_symlink_if_ours "$ROOT/.cursor/skills/$name" "$name"
done

if [[ -f "$ROOT/.cursor/hooks.json" ]] && same_inode "$ROOT/.cursor/hooks.json" "$ROOT/hooks/cursor-hooks.json"; then
  rm -f "$ROOT/.cursor/hooks.json"
fi

if [[ -f "$ROOT/.cursor/mcp.json" ]] && same_inode "$ROOT/.cursor/mcp.json" "$ROOT/mcp.json"; then
  rm -f "$ROOT/.cursor/mcp.json"
fi

echo "Removing global mirrors under $USER_CURSOR/ (only files still linked to this plugin)"
for f in build-feature design fix-bug init-repo; do
  c="$USER_CURSOR/commands/$f.md"
  if [[ -f "$c" ]] && same_inode "$c" "$ROOT/commands/$f.md"; then
    rm -f "$c"
  fi
done

for f in "$ROOT/agents"/*.md; do
  [[ -f "$f" ]] || continue
  b="$(basename "$f")"
  a="$USER_CURSOR/agents/$b"
  if [[ -f "$a" ]] && same_inode "$a" "$f"; then
    rm -f "$a"
  fi
done

for d in "$ROOT/skills"/*/; do
  [[ -d "$d" ]] || continue
  name="$(basename "$d")"
  remove_skill_symlink_if_ours "$USER_CURSOR/skills/$name" "$name"
done

for dir in "$ROOT/.cursor/commands" "$ROOT/.cursor/agents" "$ROOT/.cursor/rules" "$ROOT/.cursor/skills"; do
  if dir_empty "$dir"; then
    rmdir "$dir" 2>/dev/null || true
  fi
done

if dir_empty "$ROOT/.cursor"; then
  rmdir "$ROOT/.cursor" 2>/dev/null || true
fi

echo "Done. Restart Cursor (or Developer: Reload Window)."
echo "Note: Source files under $ROOT (commands, agents, rules, skills) are unchanged."
