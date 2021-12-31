from django.contrib import admin
from django.urls import path
from api import views

urlpatterns= [
    path('studentlist/',views.StudentList.as_view(),name="studentslist"),
    path('studentcreate/',views.StudentCreate.as_view(),name="studentsadd"),
    path('studentretrieve/<int:pk>/',views.StudentRetrieve.as_view(),name="studentget"),
    path('studentupdate/<int:pk>',views.StudentUpdate.as_view(),name="studentupdate"),
    path('studentlistcreate/',views.StudentListCreate.as_view(),name="studentlistcreate"),
    path('studentretrieveupdate/<int:pk>',views.StudentRetrieveUpdate.as_view(),name="studentgetupdate"),
    path('studentdestroy/<int:pk>',views.StudentRetrieveDestroy.as_view(),name="studentdelete"),
    path('studentupdatedestroy/<int:pk>',views.StudentRetrieveUpdateDestroy.as_view(),name="studentupdatedelete"),

]