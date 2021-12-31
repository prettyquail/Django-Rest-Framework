from django.shortcuts import render
from .models import Musician
from .serializers import MusicianSerializer, SingerSerializer , SongSerializer ,PersonSerializer
from rest_framework.renderers import JSONRenderer
from .models import *
from rest_framework import viewsets
from .serializers import *

from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here

# **************************Serializer class*************************
# Model Object - single musician data
def musician_detail(request, pk):
    mus= Musician.objects.get(id=pk)
    # print(stu)
    serializer = MusicianSerializer(mus)
    # print(serializer)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return JsonResponse(seriliazer.data)
    return HttpResponse(json_data, content_type='application/json')

def musician_list(request):
    mus = Musician.objects.all()
    # print(mus)
    serializer = MusicianSerializer(mus,many=True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JsonRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)


# **************************ModelSerializer****************************
class SingerViewSet(viewsets.ModelViewSet):
    queryset= Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# ***********************Hyperlinked Model Serializer************************
class PersonModelViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer