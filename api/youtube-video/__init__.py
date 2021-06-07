from flask_restx import Namespace

yt_videos_ns = Namespace("Youtube", description="get videos")

from . import routes  # noqa : F401
