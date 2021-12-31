from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import *
from rest_framework.mixins import *

# Create your views here.
class EmployeeList(GenericAPIView, ListModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args ,**kwargs)

class EmployeeCreate(GenericAPIView, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request, *args ,**kwargs)

class EmployeeRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args ,**kwargs)

class EmployeeUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args ,**kwargs)

class EmployeeDestroy(GenericAPIView, DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args ,**kwargs)