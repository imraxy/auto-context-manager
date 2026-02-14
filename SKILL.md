# Auto Context Manager

AI-powered automatic project context management. Detects which project the user is referring to and maintains context awareness.

## Activation

**Auto-detect on:** Use at session start or when context is unclear.
**Manual call:** When user asks about projects or context switching.

## Quick Commands

Run from `skills/auto-context-manager/`:

```bash
# Detect project from message
python acm.py detect "your message here"

# List all projects
python acm.py list

# Get current active project
python acm.py current

# Switch to different project
python acm.py switch <project_id>
```

## Available Projects

| Project | Description | Keywords |
|---------|-------------|----------|
| `trading` | Crypto & Binance | binance, crypto, position, pnl, profit, loss, btc, futures, portfolio |
| `clawdbot` | Bot development | gateway, skill, config, whatsapp, jarvis, status, restart, session |
| `skills` | Skill creation | skill, agent, context, memory, python, create skill |
| `network` | Pi infrastructure | pi, jarvis.local, docker, mqtt, 192.168, api, server |
| `default` | General | hello, help, general |

## Usage in Sessions

**When user message contains project keywords:**
1. Run `python acm.py detect "<message>"` to identify context
2. Use context to prioritize relevant skills/memory
3. Respond with project-aware knowledge

**Example:**
```
User: "Check my binance positions"
→ Detect: trading (11% confidence)
→ Use binance-pro / binance-portfolio skills
→ Check trading-related memory files
```

## Files

- `auto_context_manager.py` - Core module
- `acm.py` - CLI wrapper
- `~/.auto-context/projects.json` - Project config (auto-created)

## Adding Projects

```python
from auto_context_manager import AutoContextManager
acm = AutoContextManager()
acm.create_project('project_id', 'Project Name', ['keyword1', 'keyword2'], 'Description')
```

## Integration Notes

- Fully local, no external APIs
- Data stored in `~/.auto-context/`
- Confidence score indicates match strength
- Always returns a result (defaults to "default" project)