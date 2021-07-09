from django.urls import path
from .views import *

urlpatterns = [
    path('students/', student_list, name="students"),
    path('teachers/', teachers_list, name="teachers"),
    path('teachers/<int:id>/', teacher_detail, name='teacher_detail'),
    path('rooms/', xona_list, name="rooms"),
    path('forms/', student_form, name='forms')
]