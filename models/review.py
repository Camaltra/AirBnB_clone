#!/usr/bin/python3
"""
Module for Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    The class Review inherits of BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
