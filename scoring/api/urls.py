from django.urls import path, re_path
from api import views

urlpatterns = [
    path('', views.HomeView.as_view()),

]