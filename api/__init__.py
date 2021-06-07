import logging
from traceback import format_exc

from werkzeug.exceptions import HTTPException

from config import config
from flask import Flask, request
from flask_marshmallow import Marshmallow
from flask_restx import Api
from mongoengine import connect

from core.common import json_response

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

ma = Marshmallow()
CONFIG = ""


def create_app(env, additional_settings=None):
    global CONFIG
    if additional_settings is None:
        additional_settings = {}
    logger.info('Environment in __init__: "%s"', env)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[env])
    CONFIG = config[env]
    config[env].init_app(app)
    app.config.update(additional_settings)
    app.url_map.strict_slashes = False
    # Register all the extension here
    api = Api(
        doc=CONFIG.SWAGGER_DOCS,
    )
    connect("yt_video",host="mongodb://mongodb/yt_video")
    ma.init_app(app)

    from api.youtube_video import yt_videos_ns

    api.add_namespace(yt_videos_ns, path="/yt-videos")


    from core.management.commands import dump_yt_data, mongo

    app.cli.add_command(mongo)
    app.cli.add_command(dump_yt_data)

    # @app.errorhandler(Exception)
    # def handle_internal_server_exception(error):
    #     """Return error and status code"""
    #     request_dict = request.__dict__["environ"]
    #     code = 500
    #     message = "Something went wrong"
    #     if isinstance(error, HTTPException):
    #         message = error.description
    #         code = error.code
    #
    #     # This block added to dump error during development.
    #     if CONFIG.ENV == "dev":
    #         print(format_exc())
    #
    #     request_dict.update(
    #         {"status_code": code, "exceptions": format_exc(), "error_log_dump": True}
    #     )
    #
    #     return json_response(code, msg=message)

    api.init_app(app)
    return app
