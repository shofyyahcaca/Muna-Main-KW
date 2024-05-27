from django.http import JsonResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Muna.Model import SINAU_DB
from datetime import datetime
from Muna.Model.sinau import Student, StudyPrograms, Lecture, WorkUnit, LectureUnit, ScienceConsortium, ScienceLecture
import uuid, json, re

engine = create_engine(SINAU_DB)
Session = sessionmaker(bind=engine)

def split_text(text:str):
    pattern = r'\((.*?)\)'
    inSideArr = re.findall(pattern, text)
    outSide = re.sub(pattern, '', text).strip().lower()
    inSide = ' '.join(inSideArr).strip().lower()
    return inSide, outSide

def lecture(data):
    session = Session()
    if data:
        try:
            works = list(dict.fromkeys(value.get("Unit Kerja") for value in data if value.get("Unit Kerja")))
            sciences = list(dict.fromkeys(value.get("Konsorsium Ilmu") for value in data if value.get("Konsorsium Ilmu")))
            workResults = session.query(WorkUnit).filter(WorkUnit.unit.in_(works)).all()
            scienceResults = session.query(ScienceConsortium).filter(ScienceConsortium.scico.in_(sciences)).all()
            lectureRelation = []
            for value in data:
                lecture = Lecture(
                    lecture_uuid=str(uuid.uuid4()),
                    name=value.get("Nama"),
                    nip=value.get("NIP")
                )
                session.add(lecture)
                unit = value.get("Unit Kerja")
                ilmu = value.get("Konsorsium Ilmu")
                work = [result for result in workResults if unit == result.unit]
                science = [result for result in scienceResults if ilmu == result.scico]
                if not work:
                    work = WorkUnit(unit=unit)
                    session.add(work)
                    workResults.append(work)
                else:
                    work = work[0]
                if not science:
                    science = ScienceConsortium(scico=ilmu)
                    session.add(science)
                    scienceResults.append(science)
                else:
                    science = science[0]
                lectureRelation.append({
                    "lecture":lecture,
                    "work": work,
                    "science": science
                })
            session.commit()
            for relation in lectureRelation:
                lecture = relation.get("lecture")
                work = relation.get("work")
                science = relation.get("science")
                unit = LectureUnit(worun_id=work.worun_id, lecture_id=lecture.lecture_id)
                scien = ScienceLecture(scico_id=science.scico_id, lecture_id=lecture.lecture_id)
                session.add(unit)
                session.add(scien)
            session.commit()
            response = {"message": "success"}
        except Exception as e:
            session.rollback()
            response = {"message": "error", "details": str(e)}
        finally:
            session.close()
    else:
        response = {"message": "data tidak valid"}
    return JsonResponse(response)

def student(data):
    session = Session()
    if data:
        try:
            prod = list(dict.fromkeys(value.get("program studi") for value in data if value.get("program studi")))
            stupro = []
            for value in prod:
                inSide, outSide = split_text(value)
                stupro.append({
                    "inSide": inSide, 
                    "outSide": outSide
                })
            stuproResult = session.query(StudyPrograms).filter(StudyPrograms.name.in_([value["outSide"] for value in stupro]))
            stuproName = [st.name for st in stuproResult]
            stuproModel = [model for model in stuproResult]
            for value in stupro:
                if value["outSide"] not in stuproName:
                    inSide = value["inSide"]  if str(value["inSide"]).strip != '' else "-"
                    st = StudyPrograms(name=value["outSide"] ,alias=inSide)
                    session.add(st)
                    stuproModel.append(st)
            session.commit()
            for value in data:
                time = int(datetime.now().timestamp())
                _, outSide = split_text(value.get("program studi"))
                st = [st for st in stuproResult if st.name == outSide][0]
                student = Student(
                    stupro_id= st.stupro_id,
                    student_uuid=str(uuid.uuid4()),
                    nim= value.get("nim"),
                    name= value.get("nama"),
                    jenjang= value.get("jenjang"),
                    semester= int(value.get("semester")),
                    created_at= time,
                    updated_at= time
                )
                session.add(student)
            session.commit()
            response = {"message": "success"}
        except Exception as e:
            session.rollback()
            response = {"message": "error", "details": str(e)}
        finally:
            session.close()
    else:
        response = {"message": "data tidak valid"}
    return JsonResponse(response)

def courses(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)

def thesis(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)
