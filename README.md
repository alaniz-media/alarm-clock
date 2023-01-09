# alaniz-media: alarm-clock

Internet search, data aggregation, and analytics tool.

## Getting Started

- **Clone the repo:** `git clone git@github.com:alaniz-media/alarm-clock.git`
- **Create a virtual environment:** `python3 -m venv .venv`
- **Install requirements:** `pip3 install -r requirements.txt`

## Running

Requires command line access to a system where you can run python3 scripts.

Call with `python3 ./scraper/web_scraper.py [url] [options]`

Example: `python3 ./scraper/web_scraper.py https://www.tiktok.com/t/ZTRgF1U9M/ av`

Options:
 - `av`: return audio and video **(only option currently)**
 - `a`: return audio only _(currently not supported)_
 - `v`: return video only _(currently not supported)_

## Current Limitations

**Platforms:**
Currently `alarm-clock` only supports scraping from tiktok.com. It can be extended to support other platforms.

**File Formats:**

See options above.
