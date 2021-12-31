from django.contrib import admin
from django.urls import path
from mixins import views

urlpatterns= [
    path('emplist/',views.EmployeeList.as_view(),name="emplist"),
    path('empcreate/',views.EmployeeCreate.as_view(),name="empadd"),
    path('empretrieve/<int:pk>/',views.EmployeeRetrieve.as_view(),name="studentget"),
    path('empupdate/<int:pk>',views.EmployeeUpdate.as_view(),name="studentupdate"),
    path('empdelete/<int:pk>',views.EmployeeDestroy.as_view(),name="studentlistcreate"),

]