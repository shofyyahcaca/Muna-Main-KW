from django.http import JsonResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Muna.Model import SINAU_DB, MUNAQASYAH_DB
from Muna.Model.sinau import Lecture
from Muna.Model.munaqasyah import Course


sinauEngine = create_engine(SINAU_DB)
SinauSession = sessionmaker(bind=sinauEngine)
muanEngine = create_engine(MUNAQASYAH_DB)
MunaSession = sessionmaker(bind=muanEngine)

def getData():
    munaSession = MunaSession()
    sinauSession = SinauSession()
    try:
        lecture = sinauSession.query(Lecture).all()
        course = munaSession.query(Course).all()
        lectureCourse = []
        for lec in lecture:
            lectureCourse.append({
                "nama"  : lec.name,
                "nip"   : lec.nip,
                "senin" : [{"start time":cour.start_time, "end time":cour.end_time} for cour in course if cour.day == "Senin" and cour.lecture_uuid == lec.lecture_uuid],
                "selasa": [{"start time":cour.start_time, "end time":cour.end_time} for cour in course if cour.day == "Selasa" and cour.lecture_uuid == lec.lecture_uuid],
                "rabu"  : [{"start time":cour.start_time, "end time":cour.end_time} for cour in course if cour.day == "Rabu" and cour.lecture_uuid == lec.lecture_uuid],
                "kamis" : [{"start time":cour.start_time, "end time":cour.end_time} for cour in course if cour.day == "Kamis" and cour.lecture_uuid == lec.lecture_uuid],
                "jumat" : [{"start time":cour.start_time, "end time":cour.end_time} for cour in course if cour.day == "Jumat" and cour.lecture_uuid == lec.lecture_uuid]
            })
        response = {"message": "success", "data": lectureCourse}
    except Exception as e:
        response = {"message": "error", "details": str(e)}
    finally:
        munaSession.close()
        sinauSession.close()
    return JsonResponse(response)

def postData(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)
