from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.accounts,name="accounts"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
]
