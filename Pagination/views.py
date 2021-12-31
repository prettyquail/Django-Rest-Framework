from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# from rest_framework.settings import api_settings as pagination_settings

# Create your views here.

# Pagination on all views
# need to insert code in settings.py file
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# To apply pagination on separate views
# delete the default pagination code provided in the settings.py file
class MyPageNumberPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'p'

    # Allows user to change number of responses he or she wants to see over a page
    page_size_query_param = 'records'

    # to set maximum limit of data. If user selects greater than 7 value ,then it will not show more than 7 values
    max_page_size = 7

    # to use another keyword in place of 'last'
    last_page_strings = 'end'

class UserList1(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPageNumberPagination

# -----------------LimitOffset Pagination Starts------------------------

from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5

    # if we want to change default "limit" to user defined attribute name
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit =6


class UserListLimitOffset(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = LimitOffsetPagination
    pagination_class = MyLimitOffsetPagination


# -------------------Cursor Pagination starts---------------------------
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'

class UserListCursor(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # pagination_class = LimitOffsetPagination
    pagination_class = MyCursorPagination



