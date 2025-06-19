<div align="center">
    <img src="image/IMG_2811.jpeg" width="32%">
    <h1>UserInfo (VAUL3T)</h1>
    <a href="https://www.gnu.org/licenses/gpl-3.0.html">
  <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" alt="License: GPL v3">
</a>
</div>
<br>

UserInfo is a free open-source scraper with easy interface and no confusing bullshit 

Copyright (C) 2025 VAUL3T
VAUL3T@proton.me

VAUL3T is an open source project dedicated to developing OSINT tools. We provide full access to the source code to support bug hunting and to demonstrate our strict zero
knowledge policy.

We guarantee that we do not collect any data that can be linked back to you.

Only in rare cases such as when enabling anti–rate limiting features we may require your Telegram username.

Please note: All our projects are licensed under (GPLv3) 

> [!NOTE]
> We are not responsible for any damange done by modified versions, 
> We only offer support and guarantee for our ORIGINAL service.

Table of Contents
------------------

1. [Further Documentation](#further-documentation)
2. [How To Use](#how-to-use)
3. [Rate Limit](#rate-limit)
4. [Member Check](#member-check)
12. [GNU (General public license)](#license)

Further documentation
----------------------
- Website: - 
- Telegram: https://t.me/vaul3t
- GitHub: https://github.com/VAUL3T/TiktokUserInfoBot

How to use
----------------------

```python
from vaul3t import config, search

config(token="OUR_API_TOKEN", wait=1)
print(search("tiktok"))
```
You can get out API token by using the  `/api` command [`Here`](https://t.me/tiktok_user_info_scraper_bot)

How to self-host
----------------------
```python
from vaul3t import config, search, selfhost

config(token="OUR_API_TOKEN", wait=1)

selfhost(
    bot_token="TELEGRAM_BOT_TOKEN",
    requireJOIN =True,
    channelID="@TEST",
    rateLimitLengh=30,
    rateLimit=3
)

selfhost("run")

```
