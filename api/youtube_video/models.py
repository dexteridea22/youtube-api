import os
from mongoengine import (
    StringField,
    URLField,
    DateTimeField,
)

from core.abstract import AuditModel
from config import config

CONFIG = config[os.getenv("ENV")]

"""
Indexes -> Full text search enabled on title,descritpion with weight of title higher in search score
"""


class VideoModel(AuditModel):
    """
    Model to handle video for youtube search
    """

    meta = {
        "db_alias": "default",
        "collection": "youtube_videos",
        "strict": True,
        "ordering": ["- published_date"],
        "indexes": [
            "-published_date",
            {"fields": ["video_id"], "unique": True},
            {
                "fields": ["$title", "$description"],
                "default_language": "english",
                "weights": {"title": 10, "content": 5},
            },
        ],
    }
    video_id = StringField()
    title = StringField()
    description = StringField()
    published_date = DateTimeField()
    thumbnailURL = URLField()
    search_query = StringField(default=CONFIG.DEFAULT_SEARCH_YT)
