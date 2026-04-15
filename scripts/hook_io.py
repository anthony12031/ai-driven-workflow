"""Shared helpers for Cursor and Claude Code hook stdin/stdout shapes."""

from __future__ import annotations

import json
from typing import Any


def tool_input(data: dict[str, Any]) -> dict[str, Any]:
    ti = data.get("tool_input")
    return ti if isinstance(ti, dict) else {}


def is_claude_pretooluse(data: dict[str, Any]) -> bool:
    return data.get("hook_event_name") == "PreToolUse"


def emit_pretooluse_allow() -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "allow",
                }
            }
        )
    )


def emit_pretooluse_deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


def emit_cursor_allow() -> None:
    print(json.dumps({"permission": "allow"}))


def emit_cursor_deny(user_message: str, agent_message: str) -> None:
    print(
        json.dumps(
            {
                "permission": "deny",
                "user_message": user_message,
                "agent_message": agent_message,
            }
        )
    )


def emit_deny(data: dict[str, Any], user_message: str, agent_message: str) -> None:
    if is_claude_pretooluse(data):
        emit_pretooluse_deny(user_message)
    else:
        emit_cursor_deny(user_message, agent_message)


def emit_allow(data: dict[str, Any]) -> None:
    if is_claude_pretooluse(data):
        emit_pretooluse_allow()
    else:
        emit_cursor_allow()
