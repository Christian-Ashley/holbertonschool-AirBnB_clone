#!/usr/bin/python3
"""we built this class"""

from models.base_model import BaseModel


class City(BaseModel):
    """we built this class on rock and roll"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)