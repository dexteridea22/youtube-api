"""
Data loader for YT search to mongo db

Contains visualizations to make cron interactive
"""

import argparse
import time, os
from datetime import datetime, timedelta
from tqdm import tqdm
from config import config
from external.youtube_data.wrapper import YoutubeWrapper
from api.youtube_video.utils import create_video

CONFIG = config[os.getenv("ENV")]


class DataDumper:
    @staticmethod
    def dump_video_to_db(search_response):
        """
        Dumps data fetched from youtube-api to db
        """
        batch_size = 1000
        count = 0
        for res in search_response:
            for search_response in tqdm(res.get("items", [])):
                video_id = search_response["id"]["videoId"]
                title = search_response["snippet"]["title"]
                description = search_response["snippet"]["description"]
                published_date = search_response["snippet"]["publishedAt"]
                thumbnailURL = search_response["snippet"]["thumbnails"]["high"]["url"]
                payload = {
                    "video_id": video_id,
                    "title": title,
                    "description": description,
                    "published_date": published_date,
                    "thumbnailURL": thumbnailURL,
                    "search_query": CONFIG.DEFAULT_SEARCH_YT,
                }
                create_video(payload)
                count += 1
        print(f"Total Dumped {count} videos")

    @staticmethod
    def register_parser():
        """
        register parser
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--q", help="Search term", default=CONFIG.DEFAULT_SEARCH_YT)
        parser.add_argument("--max-results", help="Max results", default=50)
        parser.add_argument("--type", help="video", default="video")
        parser.add_argument("--order", help="ordering", default="date")
        parser.add_argument("--first", help="first call", default=True)
        parser.add_argument(
            "--publishedAfter",
            help="All result published after this date",
            default=(
                datetime.utcnow() - timedelta(days=int(CONFIG.YOUTUBE_CRON_START_DAY))
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        return parser

    @staticmethod
    def parse_results():
        """
        Parses results
        """
        # TODO  make them async with publishedAfter called every 10 sec configutable
        parser = DataDumper.register_parser()
        flag = True
        is_first = True
        while flag:
            args = parser.parse_args()
            if not is_first:
                args.publishedAfter = (
                    datetime.utcnow()
                    - timedelta(seconds=int(CONFIG.YOUTUBE_API_CALL_LAG_IN_SECONDS))
                ).strftime("%Y-%m-%dT%H:%M:%SZ")
            print("=======Initiated========")
            response = YoutubeWrapper.search(args)
            DataDumper.dump_video_to_db(response)
            time.sleep(int(CONFIG.YOUTUBE_API_CALL_LAG_IN_SECONDS))
            print("=======Processed========")
            print("=======Waiting...========")
            is_first = False


"""
Cron initiater
"""


def go(**kwargs):
    DataDumper.parse_results()


if __name__ == "__main__":
    go()
