from bson import ObjectId
from flask_restx import reqparse, inputs

search_parser = reqparse.RequestParser()
search_parser.add_argument(
    "id",
    type=ObjectId,
    location="args",
    action="append",
    help="ObjectId of Model",
    default=[],
)
search_parser.add_argument(
    "query",
    type=inputs.regex("^[A-Za-z0-9 _]*[A-Za-z0-9][A-Za-z0-9 _]*$"),
    location="args",
    trim=True,
    default="",
)
search_parser.add_argument("limit", type=inputs.positive, location="args")

video_list_parser = reqparse.RequestParser()
video_list_parser.add_argument(
    "id",
    type=ObjectId,
    location="args",
    action="append",
    help="ObjectId of Model",
)
video_list_parser.add_argument("page", type=inputs.positive, location="args", trim=True)
video_list_parser.add_argument(
    "pageSize", type=inputs.positive, location="args", trim=True
)
video_list_parser.add_argument(
    "sortOrder", type=str, choices=("ascend", "descend"), location="args", trim=True
)
video_list_parser.add_argument(
    "sortField",
    type=str,
    choices=("name", "published_date"),
    location="args",
    trim=True,
)
