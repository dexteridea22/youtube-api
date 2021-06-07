import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class Config:
    SWAGGER_DOCS = "/docs"
    DEBUG = False
    ENV = os.getenv("ENV")
    PROPAGATE_EXCEPTIONS = True
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOAD_FOLDER = "/tmp"
    PAGE_SIZE = 50

    SEARCH_LIMIT = 20
    YOUTUBE_CRON_START_DAY = os.getenv("YOUTUBE_CRON_START_DAY")
    YOUTUBE_API_CALL_LAG_IN_SECONDS = os.getenv("YOUTUBE_API_CALL_LAG_IN_SECONDS")
    DEFAULT_SEARCH_YT = "Football|Cricket"

    # MAX RETRIES, TIME OUT FOR REQUESTS
    REQUESTS_TIMEOUT_SECONDS = 15
    REQUESTS_MAX_RETRIES = 0

    MONGO_URI = os.getenv("DB_URI", "localhost")
    MONGODB_SETTINGS = [
        {
            "ALIAS": "default",
            "DB": "yt_video",
            "HOST": os.environ.get("DB_URI", "localhost"),
            "PORT": int(os.environ.get("DB_PORT", 27017)),
        },
        {
            "ALIAS": "raw_database",
            "DB": "raw_database",
            "HOST": os.environ.get("RAW_DATABASE_URI", "localhost"),
            "PORT": int(os.environ.get("RAW_DATABASE_PORT", 27017)),
        },
    ]

    DEVELOPER_KEY = os.getenv("DEVELOPER_KEY")
    YOUTUBE_API_SERVICE_NAME = os.getenv("YOUTUBE_API_SERVICE_NAME")
    YOUTUBE_API_VERSION = os.getenv("YOUTUBE_API_VERSION")

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    SWAGGER_DOCS = False
    DEBUG = False


config = {"dev": DevConfig, "test": TestConfig, "prod": ProdConfig}
