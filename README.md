# Discord Logger

[![PyPI](https://img.shields.io/pypi/v/discord-logger)](https://pypi.org/project/baihu-discord-logger/)
[![Python](https://img.shields.io/pypi/pyversions/discord-logger)](https://pypi.org/project/baihu-discord-logger/)
[![License](https://img.shields.io/github/license/baihufox3210/discord-logger)](https://github.com/baihufox3210/discord-logger/blob/main/LICENSE)

Simple Discord webhook logger for Python.

## Installation

```bash
pip install discord-logger
```

## Usage

```python
from discord_logger import DiscordLogger

logger = DiscordLogger(webhook_url = "YOUR_WEBHOOK_URL")

logger.info(title = "Server", description = "Server started")
logger.error(title = "Database", description = "Database crashed")
```

## License

MIT License