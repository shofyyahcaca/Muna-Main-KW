from django.http import JsonResponse

def lecture(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)

def student(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)

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
