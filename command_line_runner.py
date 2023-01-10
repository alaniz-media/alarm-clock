"""Local Runner - For testing the backend locally.
"""

import sys

from api.video_to_audio import video_to_audio
from scraper.web_scraper import download_content


def save_file_to_system(url: str, output: str = "video"):
    """
        url: This should be the url from a page on which a single video is present.
        output:   - av: Audio and Video
                  -  v: Video Only
                  -  a: Audio Only
    """
    print(f"Attempting to save {output} file from url: {url}\n")
    # TODO: Get a video name from the user or from the page.
    print("WARNING: Different clips are going to have the same file name instead of a unique name for each file.")

    video_file = download_content(url, output)
    with open("video_clip.mp4", 'wb') as opened_video:
        opened_video.write(video_file)

    if output == "audio":
        processed_audio, processed_video = video_to_audio("./video_clip.mp4")
        processed_audio.write_audiofile("audio_clip.mp3")
        processed_audio.close()
        processed_video.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ERROR: Must pass in URL to scrape. Optionally pass 2nd param: a,v, or av")
        print("example: python3 command_line_runner.py https://www.tiktok.com/t/ZTRgF1U9M/ video")
        sys.exit(1)

    if len(sys.argv) < 3 or sys.argv[2] not in ["audio", "video"]:
        print("ERROR: Must pass in output format of 'audio' or 'video'")
        print("example: python3 command_line_runner.py https://www.tiktok.com/t/ZTRgF1U9M/ audio")
        sys.exit(1)

    url = sys.argv[1]
    output_format = sys.argv[2]
    save_file_to_system(url, output_format)
