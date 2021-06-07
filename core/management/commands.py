"""
Mangements command
"""
from click import group

from core.batch.yt_data.dump_videos import go as fetch_and_dump


@group(name="mongo")
def mongo():
    """All mongo custom commands"""
    pass


@mongo.command("dump_yt_data")
def dump_yt_data():
    """
    Batch job to fetch and dump youtube data on predefined search
    """
    fetch_and_dump()
