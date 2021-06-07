"""
Route registering and main entry point
"""

from flask_restx import Resource

from core.parser import video_list_parser, search_parser
from core.common import json_response
from api import CONFIG


from . import yt_videos_ns
from .utils import (
    list_videos,
    search_videos,
)
from .schemas import VideoSchema


@yt_videos_ns.route("/v1/videos")
class VideoList(Resource):
    @yt_videos_ns.expect(video_list_parser)
    @yt_videos_ns.doc(
        responses={200: "Ok", 422: "Validation Error", 500: "Internal Server Error"}
    )
    def get(self):
        """
            Description: List Videos YT
        :return: Json response of List of YT videos
        """
        query_arguments = video_list_parser.parse_args()
        fields = (
            "video_id",
            "title",
            "description",
            "published_date",
            "thumbnailURL",
            "created_at",
            "modified_at",
        )
        videos = list_videos(query_arguments=query_arguments, fields=fields)
        page = videos.page
        total = videos.total
        video_schema = VideoSchema(many=True, only=fields)
        videos = video_schema.dump(videos.items)

        return json_response(
            200,
            data={
                "data": videos,
                "page": page,
                "items_on_page": len(videos),
                "count": query_arguments["pageSize"]
                if query_arguments["pageSize"]
                and query_arguments["pageSize"] < CONFIG.PAGE_SIZE + 1
                else CONFIG.PAGE_SIZE,
                "total": total,
            },
        )


@yt_videos_ns.route("/v1/search")
class VideoSearch(Resource):
    @yt_videos_ns.expect(search_parser)
    @yt_videos_ns.doc(
        responses={201: "Ok", 422: "Validation Error", 500: "Internal Server Error"}
    )
    def get(self):
        """
            List Searched YT videos
        :return: Json response
        """
        query_arguments = search_parser.parse_args()
        videos = search_videos(query_arguments)

        videos_schema = VideoSchema(
            many=True, only=("video_id", "title", "description", "published_date")
        )
        videos = videos_schema.dump(videos)

        videos = list(
            map(
                lambda item: {
                    "title": item["title"],
                    "description": item["description"],
                    "published_date": item["published_date"],
                },
                videos,
            )
        )
        return json_response(
            200,
            data={
                "results": videos,
            },
        )
