from rest_framework import serializers
from .models import *

# **********************Serializer*************************
class MusicianSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    instrument = serializers.CharField(max_length=100)

# ---------------------ModelSerializer-------------------


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']

class SingerSerializer(serializers.ModelSerializer):
    song= serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id','name','gender','song']


# *************************Hyperlinked Model Serializer*********************************
class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id','url','firstname','lastname','city']