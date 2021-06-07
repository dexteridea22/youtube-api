"""
Wrapper youtube data API V3
"""


from googleapiclient.discovery import build


import os

from config import config

CONFIG = config[os.getenv("ENV")]


# TODO configure multiple API keys
class YoutubeWrapper:
    """
    Wraps Youtube API calls , Add new methods for this API here
    """

    DEVELOPER_KEY = CONFIG.DEVELOPER_KEY
    YOUTUBE_API_SERVICE_NAME = CONFIG.YOUTUBE_API_SERVICE_NAME
    YOUTUBE_API_VERSION = CONFIG.YOUTUBE_API_VERSION

    def __init__(self):
        pass

    @staticmethod
    def search(options):
        """
        YT search API
        :param options: parser args
        :return: list of search response
        """
        search_result = []
        youtube = build(
            YoutubeWrapper.YOUTUBE_API_SERVICE_NAME,
            YoutubeWrapper.YOUTUBE_API_VERSION,
            developerKey=YoutubeWrapper.DEVELOPER_KEY,
        )
        # Call the search.list method to retrieve results matching the specified
        # query term.
        if options.first:
            search_response = (
                youtube.search()
                .list(
                    q=options.q,
                    part="id,snippet",
                    maxResults=options.max_results,
                    publishedAfter=options.publishedAfter,
                    order=options.order,
                    type=options.type,
                )
                .execute()
            )
            search_result.append(search_response)
            flag = True
            """
            Iterate over all pages of this search response
            """
            while flag:
                pageToken = search_response.get("nextPageToken", False)
                if pageToken:
                    search_response = (
                        youtube.search()
                        .list(
                            q=options.q,
                            part="id,snippet",
                            maxResults=options.max_results,
                            publishedAfter=options.publishedAfter,
                            order=options.order,
                            type=options.type,
                            pageToken=pageToken,
                        )
                        .execute()
                    )
                    search_result.append(search_response)
                else:
                    flag = False
        return search_result
