from api import ma

from marshmallow import fields as ma_fields


class VideoSchema(ma.Schema):
    """
    Schema to handle the serialization/deserialization of video data
    """

    video_id = ma_fields.String()
    title = ma_fields.String()
    description = ma_fields.String()
    published_date = ma_fields.DateTime()
    thumbnailURL = ma_fields.Url()
    created_at = ma_fields.DateTime()
    modified_at = ma_fields.DateTime()
