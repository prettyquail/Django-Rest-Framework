from django.contrib import admin
from django.urls import path
from Pagination import views

urlpatterns= [
    path('userlist1/',views.UserList1.as_view(),name="userlist1"),
    path('userlist/',views.UserList.as_view(),name="userlist"),
    path('userlist2/',views.UserListLimitOffset.as_view(),name="userlist2"),
    path('userlist3/', views.UserListCursor.as_view(), name="userlist3"),

]