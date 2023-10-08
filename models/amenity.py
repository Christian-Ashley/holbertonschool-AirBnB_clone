#!/usr/bin/python3
"""hope my next apartment has this class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """is this some kind of airbnb thing i am too broke to understand?"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)