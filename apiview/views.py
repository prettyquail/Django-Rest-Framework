from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CarsSerializer
from rest_framework.throttling import UserRateThrottle
from .models import Cars


class CarsAPIView(APIView):
    serializer_class = CarsSerializer
    throttle_scope = "cars_app"

    def get_queryset(self):
        cars = Cars.objects.all()
        return cars

    def get(self, request,pk, format=None):

        try:
            pk = request.query_params["id"]
            if pk != None:
                car = Cars.objects.get(id=pk)
                serializer = CarsSerializer(car)
        except:
            cars = self.get_queryset()
            serializer = CarsSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data

        new_car = Cars.objects.create(car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()

        serializer = CarsSerializer(new_car)

        return Response(serializer.data)

    def put(self, request, pk ,format=None):
        id = pk
        car_object = Cars.objects.get(pk=id)
        serializer = CarsSerializer(car_object,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk, format=None):
        id =pk
        car_object = Cars.objects.get(pk=id)
        serializer = CarsSerializer(car_object, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk ,format=None):
        id =pk
        car_object = Cars.objects.get(pk=id)
        car_object.delete()
        return Response({'msg':'Data Deleted'})
