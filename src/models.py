import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    userName = Column(String(25), unique=True)
    firstName = Column(String(30), nullable=False)
    lastName = Column(String(30), nullable=True)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.user_id'))
    user_from_idRelationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.user_id'))
    user_to_idRelationship = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(180), nullable=False)
    author_id = Column(Integer, ForeignKey('user.user_id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author_idRelationship = relationship(User)
    post_idRelationship = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    type = Column(String(15), nullable=True)
    url = Column(String(100), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_idRelationship = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
