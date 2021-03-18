from rest_framework import viewsets
from rest_framework import permissions
from restapi.api.models import MyTopicMovie, Movie
from restapi.api.serializers import MyTopicMovieSerializer,MovieSerializers

from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class MyTopicMovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicMovie.objects.all()
    serializer_class = MyTopicMovieSerializer

    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def search(self, request):
        q = request.query_params.get('q',None)
        qs = self.get_queryset().filter(title=q)
        serializer = self.get_serializer(qs,many=True)

        return Response(serializer.data)

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MyTopicMovieSerializer

    permission_classes = [permissions.IsAuthenticated]
