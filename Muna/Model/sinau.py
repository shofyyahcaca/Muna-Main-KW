from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Study_programs(Base):
    __tablename__ = 'study_programs'

    stupro_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(5), nullable=False)


class Courses(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(6), nullable=False)
    stupro_id = Column(Integer, ForeignKey('study_programs.stupro_id'), nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)

    stupro = relationship("Study_programs", back_populates="courses")


class Group_classes(Base):
    __tablename__ = 'group_classes'

    grocla_id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(30), nullable=False)
    alias_pos = Column(String(4), nullable=False)
    classGroup = Column(String(4), name='class', nullable=False)


class Lecture(Base):
    __tablename__ = "lecture"

    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(5), nullable=False)
