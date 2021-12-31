from django.shortcuts import render
from Pagination.models import User
from .models import Student
from Pagination.serializers import UserSerializer
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication,SessionAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser, IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission
# Create your views here.


# **************Basic Authentication******************

class UserModelViewSet1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# If we want to apply this basic authentication to all the functions
# Then we can use global settings method in settings.py file


class UserModelViewSet2(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# If we want to override global settings
# and to allow any user to access api's
class UserModelViewSet3(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

# and to allow only specific users, whose user.is_staff is activated


class UserModelViewSet4(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


# **************************Session Authentication****************************
# AllowAny, IsAuthenticated, SessionAuthentication

class UserModelViewSet5(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]


# IsAuthenticatedOrReadOnly
class UserModelViewSet6(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


# DjangoModelPermissions
class UserModelViewSet7(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]


# DjangoModelPermissions
class UserModelViewSet8(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# Custom Permission
class UserModelViewSet9(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]


# ***********************TOKEN AUTHENTICATION**********************
class UserModelViewSet10(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Generating Token using Signals
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ****************CUSTOM AUTHENTICATION************************


from Authentication.customauth import CustomAuthentication

class StudentModelViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [ CustomAuthentication]
    permission_classes = [IsAuthenticated]


# ********************JWT TOKEN AUTHENTICATION*******************8
# from rest_framework_simplejwt.authentication import JWTAuthentication
#
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]