


from django.urls import path
# Create your models here.
from .views import LoginView,CreateUserView,CartView,UploadPhotoView,ProductView,CreatePayment
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login',csrf_exempt(LoginView.as_view()), name="login"),
    path('signup',csrf_exempt(CreateUserView.as_view()), name="login"),
    path('cart/<int:user_id>',csrf_exempt(CartView.as_view()), name="cart"),
    path('avatar/<int:user_id>',csrf_exempt(UploadPhotoView.as_view()), name="avatar"),
    path('products',csrf_exempt(ProductView.as_view()), name="avatar"),
    path('stripe',csrf_exempt(CreatePayment.as_view()), name="payment"),
]