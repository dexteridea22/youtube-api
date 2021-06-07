import os
from core import pagination
from api.youtube_video.models import VideoModel
from config import  config
CONFIG = config[os.getenv("ENV")]

def list_videos(query_arguments, fields):
    """
        List videos

    :param fields: Fields to fetch
    :param query_arguments: Query Filter Arguments
    :return: List VideoModel Object
    :rtype: List<<VideoModel>>
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
    """

    :param video_id: id of video
    :param fields: query param
    :param filters: query filter
    :param sort:  sort on
    :param limit: limit
    :return:
    """
    if video_id:
        return VideoModel.objects(**filters).only(*fields).get(id=video_id)
    return VideoModel.objects(**filters).order_by(sort).only(*fields).limit(limit)


def search_videos(query_arguments):
    """
        List Top 20 searched Videos Full text search Support

    :param query_arguments: List Arguments
    :return: List VideoModel Object
    :rtype: List<<VideoModel>>
    """

    query = query_arguments["query"]
    video_search_match = VideoModel.objects.search_text(query).order_by("$text_score")[
        :20
    ]
    return video_search_match
