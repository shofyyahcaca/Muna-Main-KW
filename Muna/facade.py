from Muna.view import auth, scraped, schedule
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
import json

from Muna.view import scraped as scraped


@method_decorator(csrf_exempt, name='dispatch')
class Register(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return auth.register(data)
    

@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return auth.login(data)


@method_decorator(csrf_exempt, name='dispatch')
class ScrapedLecture(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return scraped.lecture(data)
    

@method_decorator(csrf_exempt, name='dispatch')
class ScrapedStudent(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return scraped.student(data)
    

@method_decorator(csrf_exempt, name='dispatch')
class ScrapedCourses(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return scraped.courses(data)
    

@method_decorator(csrf_exempt, name='dispatch')
class ScrapedThesis(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return scraped.thesis(data)
    

@method_decorator(csrf_exempt, name='dispatch')
class Schedule(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        return schedule.postData(data)
    
    def get(self, request, *args, **kwargs):
        return schedule.getData()



