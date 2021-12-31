from django.shortcuts import render
from Filtering.serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user= self.request.user
        return Student.objects.filter(passby=user)



# To apply fitering in particular views
class StudentList2(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['passby']

# Search Filter
class StudentList3(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends= [SearchFilter]
    # search_fields = ['city']
    search_fields = ['^name']

# Ordering Filter
class StudentList4(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['city']