# alaniz-media: alarm-clock

Internet search, data aggregation, and analytics tool.

## Getting Started

- **Clone the repo:** `git clone git@github.com:alaniz-media/alarm-clock.git`
- **Create a virtual environment:** `python3 -m venv .venv`
- **Source the virtual environment:** `source .venv/bin/activate`
- **Install requirements:** `pip3 install -r requirements.txt`

**Note:** the `moviepy` package requires `ffmpeg` and that won't be installed automatically by the above steps. I don't love having to install either of those packages, but this is a simple proof of concept. Feel free to swap that out later with some other process. For now, you'll need to get `ffmpeg` installed on whatever system you expect to run this on.

## Running

Requires command line access to a system where you can run python3 scripts.

Call with `python3 ./scraper/web_scraper.py [url] [options]`

Example: `python3 ./scraper/web_scraper.py https://www.tiktok.com/t/ZTRgF1U9M/ video`

Options:
 - `video`: saves video file only
 - `audio`: saves video file and an audio file

## Current Limitations

**Platforms:**
Currently `alarm-clock` only supports scraping from tiktok.com. It can be extended to support other platforms.

**File Formats:** See options above.
