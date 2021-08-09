from django.urls import path
from . import views

urlpatterns = [
    path('ori/', views.Videos_ori, name="videos_ori"),
    path('sonia/', views.Videos_sonia, name="videos_sonia"),
    path('grisha/', views.Videos_grisha, name="videos_grisha"),
    path('inbar/', views.Videos_inbar, name="videos_inbar"),
    path('lila/', views.Videos_lila, name="videos_lila"),

]