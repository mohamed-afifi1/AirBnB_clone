#!/usr/bin/python3
""" module to detrmine a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the User class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
