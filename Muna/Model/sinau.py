from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Lecture(Base):
    __tablename__ = 'lecture'
    
    lecture_id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_uuid = Column(String, nullable=False)
    name = Column(String(100), nullable=False)
    nip = Column(String(20), nullable=False)


class WorkUnit(Base):
    __tablename__ = 'work_unit'
    
    worun_id = Column(Integer, primary_key=True, autoincrement=True)
    unit = Column(String(100), nullable=False)


class LectureUnit(Base):
    __tablename__ = 'lecture_unit'
    
    lecun_id = Column(Integer, primary_key=True, autoincrement=True)
    worun_id = Column(Integer, ForeignKey('work_unit.worun_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('lecture.lecture_id'), nullable=False)
    
    work_unit = relationship('WorkUnit', back_populates='lecture_units')
    lecture = relationship('Lecture', back_populates='lecture_units')


class ScienceConsortium(Base):
    __tablename__ = 'science_consortium'
    
    scico_id = Column(Integer, primary_key=True, autoincrement=True)
    scico = Column(String(100), nullable=False)


class ScienceLecture(Base):
    __tablename__ = 'science_lecture'
    
    scile_id = Column(Integer, primary_key=True, autoincrement=True)
    scico_id = Column(Integer, ForeignKey('science_consortium.scico_id'), nullable=False)
    lecture_id = Column(Integer, ForeignKey('lecture.lecture_id'), nullable=False)
    
    science_consortium = relationship('ScienceConsortium', back_populates='science_lectures')
    lecture = relationship('Lecture', back_populates='science_lectures')


class StudyPrograms(Base):
    __tablename__ = 'study_programs'
    
    stupro_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    alias = Column(String(5), nullable=False)


class Student(Base):
    __tablename__ = 'student'
    
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_uuid = Column(String, nullable=False)
    stupro_id = Column(Integer, ForeignKey('study_programs.stupro_id'), nullable=False)
    nim = Column(String(15), nullable=False)
    jenjang = Column(String(5), nullable=False)
    name = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)
    
    study_program = relationship('StudyPrograms', back_populates='students')
    theses = relationship('Thesis', backref='student_relation')


class Thesis(Base):
    __tablename__ = 'thesis'
    
    thesis_id = Column(Integer, primary_key=True, autoincrement=True)
    thesis_uuid = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.student_id'), nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)
    
    student = relationship('Student', back_populates='theses', overlaps="student_relation")


WorkUnit.lecture_units = relationship('LectureUnit', back_populates='work_unit')
Lecture.lecture_units = relationship('LectureUnit', back_populates='lecture')
ScienceConsortium.science_lectures = relationship('ScienceLecture', back_populates='science_consortium')
Lecture.science_lectures = relationship('ScienceLecture', back_populates='lecture')
StudyPrograms.students = relationship('Student', back_populates='study_program')