"""Scrapper - Get Audio and/or Video from Various Online Sources
"""

import logging
import sys
import time

import requests

from datetime import date, timedelta
from decimal import Decimal as D
from re import sub
from typing import Any, Dict, List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LOGGER = logging.getLogger(__name__)


# using a firefox user agent, betting that "Custom" or
# otherwise unofficial agents will eventually be blocked
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
REQ_HEADER = {"User-Agent": USER_AGENT}

OPTIONS = Options()
OPTIONS.add_argument('--headless')
DRIVER = webdriver.Chrome(options=OPTIONS)


def get_page_contents(url: str):
    selenium_rsp = DRIVER.get(url)
    return selenium_rsp


# Alternative if an API were provided
# def call_api(url: str):
#     print(f"GET request to: {url}")
#     try:
#         rsp = requests.get(url=url, headers=REQ_HEADER, json=None, verify=False)
#         return rsp
#     except (ConnectionError, MaxRetryError, SSLError, Timeout) as e:
#         error_msg = f"call_api exception with url: {url}"
#         LOGGER.error(error_msg)
#         LOGGER.exception(e)


def get_video_url(url: str) -> str:
    """
        url: This should be the url from a page on which a single video is present.
        This will return a direct link to the video on the CDN
    """

    selenium_rsp = get_page_contents(url)

    parse_with_beautiful_soup = False
    if parse_with_beautiful_soup:
        # TODO: This is non-deterministic. It will BOTH waste time and end up breaking when something
        # eventually takes more than 20 seconds. This may not even be waiting in a useful spot.
        # See: https://selenium-python.readthedocs.io/waits.html
        print("WARNING: Arbitrarily sleeping for 13 seconds. See code for alternatives to this.")
        time.sleep(13)
        page = DRIVER.page_source
        DRIVER.quit()
        soup = BeautifulSoup(page, 'html.parser')
        all_links_found = soup.find_all("a")
        print(f"\nFound {len(all_links_found)} links on requested page.")

        video_link_count = 0
        for link in all_links_found:
            if "mime_type=video_mp4" in link:
                video_link_count += 1
                print(link)

    else:
        # See: https://stackoverflow.com/questions/71850807/how-to-get-the-link-to-a-file-that-comes-in-on-the-network-page-on-chrome-from-s
        # And: https://stackoverflow.com/questions/45847035/using-selenium-how-to-get-network-request/45859018#45859018
        network_script = """
        var performance = window.performance || window.webkitPerformance || {};
        var network = performance.getEntries() || {};
        return network;
        """

        # TODO: This is non-deterministic. It will BOTH waste time and end up breaking when something
        # eventually takes more than 20 seconds. This may not even be waiting in a useful spot.
        # See: https://selenium-python.readthedocs.io/waits.html
        print("WARNING: Arbitrarily sleeping for 20 seconds. See code for alternatives to this.")
        time.sleep(20)

        network_requests = DRIVER.execute_script(network_script)

        identifying_str = "mime_type=video_mp4"
        # urls = [request['name'] for request_url in network_requests if identifying_str in request_url]
        all_links_found = []
        for request_x in network_requests:
            request_url = request_x["name"]
            if identifying_str in request_url and request_url not in all_links_found:
                print("\n - Match Found: ", request_url)
                all_links_found.append(request_url)
        video_link_count = len(all_links_found)

    if video_link_count > 1 :
        print(f"ERROR: Expected 1 video on page. Found {video_link_count} video links.")
        return
    elif video_link_count == 0:
        print(f"ERROR: No videos found on page")
        return

    print("Found Video URL: ", all_links_found[0])
    return all_links_found[0]


def download_content(url: str, output: str = "av"):
    """
        url: This should be the url from a page on which a single video is present.
        output:   - av: Audio and Video
                  -  v: Video Only
                  -  a: Audio Only
    """
    video_url = get_video_url(url)
    rsp = requests.get(video_url)
    # TODO: Get a video name from the user or from the page.
    print("WARNING: This is going to save as just 'exported_video.mp4'.")
    with open("exported_video.mp4", 'wb') as video:
        video.write(rsp.content)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Must pass in URL to scrape. Optionally pass 2nd param: a,v, or av")
        print("example: python3 ./scraper/web_scraper.py https://www.tiktok.com/t/ZTRgF1U9M/ v")
        sys.exit(1)

    url = sys.argv[1]
    # url = "https://www.xignite.com/xRates.json/GetRate"
    url = "https://www.tiktok.com/t/ZTRgF1U9M/"
    output_format = "av"
    if len(sys.argv) == 3:
        output_format = sys.argv[2]

    download_content(url, output_format)
