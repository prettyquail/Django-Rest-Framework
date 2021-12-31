from django.urls import path,include
from Filtering import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('filter/',views.StudentList.as_view()),
    path('filter2/',views.StudentList2.as_view()),
    path('filter3/',views.StudentList3.as_view()),
    path('filter4/',views.StudentList4.as_view()),
]