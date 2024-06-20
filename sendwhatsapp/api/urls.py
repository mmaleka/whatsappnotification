from django.urls import include, re_path
from django.urls import path, include
from . import views

app_name = 'sendwhatsapp_api'


urlpatterns = [

    path('', views.SendWhatsappAPIView.as_view(), name="SendWhatsappAPIView"),

]