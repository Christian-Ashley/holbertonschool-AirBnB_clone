#!/usr/bin/python3
"""Base Model Class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """base class for all models"""
    def __init__(self, *args, **kwargs):
        """initialize the BaseModel instance"""
        self.id = str(uuid.uuid4())