from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.


class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        print("********List*********")
        print("Basename:", self.basename)
        print("Action:",self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:",self.name)
        print("Description:", self.description)
        cust= Customer.objects.all()
        serializer = CustomerSerializer(cust , many=True)
        return Response(serializer.data)

    def retrieve(self, request , pk=None):
        id=pk
        if id is not None:
            cust= Customer.objects.get(id=id)
            serializer = CustomerSerializer(cust)
            return Response(serializer.data)

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request , pk):
        id= pk
        cust = Customer.objects.get(pk=id)
        serializer = CustomerSerializer(cust, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        id =pk
        cust = Customer.objects.get(pk=id)
        serializer=CustomerSerializer(cust, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.erros)

    def destroy(self,request,pk):
        id = pk
        cust=Customer.objects.get(pk=id)
        cust.delete()
        return Response({'msg':'Data Deleted'})


# -------------------------ModelViewSet------------------------------
class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



# -------------------------ReadOnlyModelViewSet-------------------------

class CustomerReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer