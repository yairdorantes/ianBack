from django.shortcuts import render
import json
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
UserModel = get_user_model()

# Create your views here.
class LoginView(View):
    def post(self,request):
        jd = json.loads(request.body)
        email = jd['email']
        password = jd['password']
        print(email,password)
        user  = authenticate(username=email,password=password)
        if user is not None:
            return HttpResponse("success", status=200)
        else:
            return HttpResponse("login failed.", status=401)
        # return JsonResponse({"message":"success"})

class CreateUserView(View):
    def post(self,request):
        jd = json.loads(request.body)
        user = UserModel.objects.create_user(
            username=jd['username'],
            email=jd['email'])
        user.set_password(jd['password'])
        user.save()
        return HttpResponse("success", status=200)
