import os
from core import pagination
from api.youtube_video.models import VideoModel
from api import CONFIG
from config import config
from datetime import datetime

CONFIG = config[os.getenv("ENV")]


def list_videos(query_arguments, fields):
    """
        List Prime offers

    :param fields: Fields to fetch
    :param query_arguments: Query Filter Arguments
    :return: List PrimeOfferModel Object
    :rtype: List<<PrimeOfferModel>>
    """
    videos = pagination(get_videos, query_arguments, fields)
    return videos


def get_videos(
    video_id=None,
    fields=(),
    filters={},
    sort="created_at",
    limit=CONFIG.SEARCH_LIMIT,
):
    if video_id:
        return VideoModel.objects(**filters).only(*fields).get(id=video_id)
    return VideoModel.objects(**filters).order_by(sort).only(*fields).limit(limit)


def search_videos(query_arguments):
    """
        List Top 20 searched Videos Full text search Support

    :param query_arguments: List Arguments

        query_arguments:
                - limit: To limit the count of document
                - query: For name search
                - id: List of ObjectId of `VideoModel` Model

    :return: List VideoModel Object
    :rtype: List<<VideoModel>>
    """

    query = query_arguments["query"]
    video_search_match = VideoModel.objects.search_text(query).order_by("$text_score")[
        :20
    ]
    return video_search_match
