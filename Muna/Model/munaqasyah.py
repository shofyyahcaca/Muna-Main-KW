from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .auth import User

Base = declarative_base()

class Topics(Base):
    __tablename__ = 'topics'

    topic_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)


class Topic_relation(Base):
    __tablename__ = 'topic_relation'

    toprel_id = Column(Integer, primary_key=True, autoincrement=True)
    relation = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'), nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)

    topic = relationship("Topics", back_populates="topic_relation")


class Teach_schedule(Base):
    __tablename__ = 'teach_schedule'

    teasch_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_uuid = Column(String, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)

    user = relationship(
        'User',
        backref='teach_schedule',
        primaryjoin='teach_schedule.user_uuid == User.uuid',
        foreign_keys=user_uuid,
    )


class Lecture_counter(Base):
    __tablename__ = 'lecture_counter'

    lectcount_id = Column(Integer, primary_key=True, autoincrement=True)
    user_uuid = Column(String, nullable=False)
    name = Column(Integer, nullable=False)
    first_week = Column(Integer, nullable=False)
    two_week = Column(Integer, nullable=False)
    three_week = Column(Integer, nullable=False)
    four_week = Column(Integer, nullable=False)

    user = relationship(
        'User',
        backref='lecture_counter',
        primaryjoin='lecture_counter.user_uuid == User.uuid',
        foreign_keys=user_uuid,
    )