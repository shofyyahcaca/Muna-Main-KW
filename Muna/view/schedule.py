from django.http import JsonResponse

def getData():
    return JsonResponse({
        "massage": "success",
        "data": "contoh data"
    })

def postData(data):
    if data:
        respons = {"massage": "data valid"}
    else:
        respons = {"message": "data tidak valid"}
    return JsonResponse(respons)
