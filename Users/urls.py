from django.urls import path
from .views import Register,Login,CheckEmail,CheckContactNumber,GetUser

urlpatterns = [
    path('Register',Register.as_view()),
    path('Login',Login.as_view()),
    # path('CheckEmail/<str:Email',CheckEmail.as_view()),
    path('CheckContactNumber/<str:ContactNumber>',CheckContactNumber.as_view()),
    path('CheckEmail/<str:Email>',CheckEmail.as_view()),
    path('GetUser/<str:Email>',GetUser.as_view())
]