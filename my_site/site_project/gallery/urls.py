from django.urls import path
from . import views

urlpatterns = [
    path('ori/', views.Videos_ori, name="videos_ori"),

]