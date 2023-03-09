from django.shortcuts import render
import json
import stripe

from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Cart,Product
from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
UserModel = get_user_model()

# Create your views here.
class LoginView(View):
    def post(self,request):
        jd = json.loads(request.body)
        email = jd['email']
        password = jd['password']
        # print(email,password)
        user  = authenticate(username=email,password=password)
        if user is not None:
            user_data={
                'id': user.id,
                'username': user.username,
                'email': user.email,
                "avatar":user.avatar
            }
            return JsonResponse({"success":user_data}, status=200)
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
        cart =  Cart.objects.create(user=user,products=[])
        return HttpResponse("success", status=200)

class CartView(View):
    def get(self,request,user_id):
        cart = get_object_or_404(Cart, user_id=user_id)
        response_data = {
            'cart': cart.products
        }
        # print(response_data)
        return JsonResponse(response_data)

    def put(self,request,user_id):
        jd = json.loads(request.body)
        cart = get_object_or_404(Cart, user_id=user_id)
        cart.products=jd["cart"]
        cart.save()
        return HttpResponse("success", status=200)

class UploadPhotoView(View):
    def post(self,request,user_id):
        jd = json.loads(request.body)
        user = get_object_or_404(UserModel, id=user_id)
        photo = jd['photo']
        user.avatar = photo
        user.save()
        return HttpResponse("success", status=200)

class ProductView(View):
    def get(self,request):
        products = list(Product.objects.values())
        return JsonResponse({"products":products})
stripe.api_key = "sk_test_51KjBqNA9KCn8yVMONc3gFAYwrG6HbwHVDeQ3sxLolr9K5iJHSXRmm8FXpkRFtJp7n5WWCjVjmCOlyHYObMnSVRlL00Y6KfPvVR"

class CreatePayment(View):
    def post(self,request):
        jd = json.loads(request.body)
        amount = jd["amount"]
        currency = jd["currency"]
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
        )
        client_secret = intent.client_secret
        return JsonResponse({
            "client_secret": client_secret
        })