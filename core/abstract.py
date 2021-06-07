"""
Contains Abstract classes
"""
from mongoengine import (
    Document,
    DateTimeField,
)
from datetime import datetime


class AuditModel(Document):
    """
    Abstract Model for auditing
    """

    meta = {"abstract": True}
    created_at = DateTimeField(default=datetime.now)
    modified_at = DateTimeField(default=datetime.now)
