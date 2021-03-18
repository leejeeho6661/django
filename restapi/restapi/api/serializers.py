from restapi.api.models import MyTopicMovie,Movie
from rest_framework import serializers

class MyTopicMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyTopicMovie
        fields = ['id','title','weekend','gross','weeks','genre','rating','movie_release','people','created_at']

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','weekend','gross','weeks','genre','rating','movie_release','people','created_at']