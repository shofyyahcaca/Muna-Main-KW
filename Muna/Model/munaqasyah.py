from sqlalchemy import Column, Integer, String, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Topic(Base):
    __tablename__ = 'topics'
    topic_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

class TopicRelation(Base):
    __tablename__ = 'topic_relation'
    toprel_id = Column(Integer, primary_key=True, autoincrement=True)
    thesis_uuid = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'), nullable=False)
    
    topic = relationship('Topic', back_populates='topic_relations')

Topic.topic_relations = relationship('TopicRelation', order_by=TopicRelation.toprel_id, back_populates='topic')

class Munaqasyah(Base):
    __tablename__ = 'munaqasyah'
    muna_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_uuid = Column(String, nullable=False)
    student_uuid = Column(String, nullable=False)
    munaqasyah = Column(Integer, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    courses_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_uuid = Column(String, nullable=False)
    day = Column(String(20), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)