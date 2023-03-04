


from django.urls import path
# Create your models here.
from .views import LoginView,CreateUserView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login',csrf_exempt(LoginView.as_view()), name="login"),
    path('signup',csrf_exempt(CreateUserView.as_view()), name="login"),
]