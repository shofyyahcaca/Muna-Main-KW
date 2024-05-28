from django.http import JsonResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Muna.Model import SINAU_DB, MUNAQASYAH_DB
from datetime import datetime
from Muna.Model.sinau import Student, StudyPrograms, Lecture, WorkUnit, LectureUnit, ScienceConsortium, ScienceLecture, Thesis
from Muna.Model.munaqasyah import Course, Topic, TopicRelation
import uuid, re

sinauEngine = create_engine(SINAU_DB)
SinauSession = sessionmaker(bind=sinauEngine)
muanEngine = create_engine(MUNAQASYAH_DB)
MunaSession = sessionmaker(bind=muanEngine)

def split_text(text:str):
    pattern = r'\((.*?)\)'
    inSideArr = re.findall(pattern, text)
    outSide = re.sub(pattern, '', text).strip().lower()
    inSide = ' '.join(inSideArr).strip().lower()
    return inSide, outSide

def lecture(data):
    session = SinauSession()
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
    session = SinauSession()
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
    session = MunaSession()
    sinauSession = SinauSession()
    if data:
        try:
            lecture = sinauSession.query(Lecture).all()
            notif = []
            nullValue = 0
            for value in data:
                schedule = value.get("Jadwal Mingguan")
                teach = value.get("Pengajar")
                if teach.strip() != "":
                    nip, name = [item.strip() for item in teach.split('-', 1)]
                    schedule_pattern = r"(\w+), (\d{2}:\d{2}) s\.d (\d{2}:\d{2}) @ (.+)"
                    day, start_time, end_time, _ = re.match(schedule_pattern, schedule).groups()
                    lect = [lec for lec in lecture if lec.nip == nip.strip()]
                    if lect:
                        courses = Course(
                            lecture_uuid= lect[0].lecture_uuid,
                            day= day,
                            start_time= datetime.strptime(start_time, '%H:%M').time(),
                            end_time= datetime.strptime(end_time, '%H:%M').time()
                        )
                        session.add(courses)
                    else:
                        notif.append(name)
                else:       
                    nullValue += 1
            notification = list(dict.fromkeys(value for value in notif))
            notification.append(f"{str(nullValue)} value is null")
            session.commit()
            response = {"message": "success", "missing": notification}
        except Exception as e:
            session.rollback()
            response = {"message": "error", "details": str(e)}
        finally:
            session.close()
            sinauSession.close()
    else:
        response = {"message": "data tidak valid"}
    return JsonResponse(response)

def thesis(data):
    session = MunaSession()
    sinauSession = SinauSession()
    if data:
        try:
            student = sinauSession.query(Student).all()
            topic = session.query(Topic).all()
            notif = []
            relation = []
            for value in data:
                title = value.get("judul-TA")
                name = value.get("Nama")
                nim = value.get("Nim")
                time = int(datetime.now().timestamp())
                stu = [st for st in student if st.nim == nim.strip()]
                top = re.sub(r'[^\w\s]', '', title).lower().split()
                if stu:
                    thesis = Thesis(
                        thesis_uuid= str(uuid.uuid4()),
                        student_id= stu[0].student_id,
                        title= title,
                        created_at= time,
                        updated_at= time
                    )
                    sinauSession.add(thesis)
                    for tp in top:
                        to = [t for t in topic if t.name == tp.strip()]
                        if to:
                            tpc = to[0]
                        else:
                            tpc = Topic(name=tp.strip())
                            session.add(tpc)
                            topic.append(tpc)
                        relation.append({
                            "topic": tpc,
                            "thesis": thesis
                        })
                else:
                    notif.append(name)
            notification = list(dict.fromkeys(value for value in notif))
            sinauSession.commit()
            session.commit()
            for rel in relation:
                tpcRelation = TopicRelation(thesis_uuid= rel["thesis"].thesis_uuid, topic_id=rel["topic"].topic_id)
                session.add(tpcRelation)
            session.commit()
            response = {"message": "success", "missing": notification}
        except Exception as e:
            session.rollback()
            sinauSession.rollback()
            response = {"message": "error", "details": str(e)}
        finally:
            session.close()
            sinauSession.close()
    else:
        response = {"message": "data tidak valid"}
    return JsonResponse(response)
