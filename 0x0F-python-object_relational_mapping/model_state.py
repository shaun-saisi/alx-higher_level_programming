#!/usr/bin/python3
"""Contains a class definition of a State and instance BAse"""

from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """class with id anf attributes for each state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable= False, primary_key=True)
    name = Column(String(128), nullable=False)
