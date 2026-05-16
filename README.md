# Discord Logger

[![PyPI](https://img.shields.io/pypi/v/discord-logger)](https://pypi.org/project/baihu-discord-logger/)
[![Python](https://img.shields.io/pypi/pyversions/discord-logger)](https://pypi.org/project/baihu-discord-logger/)
[![License](https://img.shields.io/github/license/baihufox3210/discord-logger)](https://github.com/baihufox3210/discord-logger/blob/main/LICENSE)

Simple Discord webhook logger for Python.

---

## Installation

```bash
pip install baihu-discord-logger
```

---

## Environment Variables (Optional)

You can configure avatars using environment variables instead of passing them in code:

- `DISCORD_OWNER_AVATAR_URL`
- `DISCORD_WEBHOOK_AVATAR_URL`

If these are not provided, the logger will default to `None`.

---

## Set Environment Variables (Permanent Only)

### Windows (PowerShell)

```powershell
setx DISCORD_OWNER_AVATAR_URL "https://example.com/owner.png"
setx DISCORD_WEBHOOK_AVATAR_URL "https://example.com/webhook.png"
```

> After setting, restart terminal or VSCode to apply changes.

---

### Linux / macOS (bash / zsh)

Add the following lines to your shell configuration file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`):

```bash
export DISCORD_OWNER_AVATAR_URL="https://example.com/owner.png"
export DISCORD_WEBHOOK_AVATAR_URL="https://example.com/webhook.png"
```

Then reload configuration:

```bash
source ~/.bashrc
```

(or restart your terminal if using zsh/macOS default shell)

---

## Usage

```python
from discord_logger import DiscordLogger

logger = DiscordLogger(webhook_url="YOUR_WEBHOOK_URL")

logger.info(title="Server", description="Server started")
logger.error(title="Database", description="Database crashed")
```

---

## License

MIT License