"""
Handle the archive related feature.
"""

from pathlib import Path
from typing import List
from simber import Logger

from ytmdl.yt import extract_video_id


# Create logger
logger = Logger("archive")


def read_archive_file(file: str) -> List:
    """
    Read the archive file and extract all the videoId's
    passed. This file will be read as text and should contain
    videoId's in each line.
    """
    file_path: Path = Path(file).expanduser()

    # Check if the file exists
    if not file_path.exists():
        logger.critical("Passed archive file does not exist. Exiting!")

    file_content: List = file_path.open().read().split("\n")
    return file_content


def is_present_in_archive(file_content: List, youtube_link: str) -> bool:
    """
    Check if the passed song is present
    in the download-archive file passed
    and accordingly return.
    """
    video_id: str = extract_video_id(youtube_link)

    return video_id in file_content