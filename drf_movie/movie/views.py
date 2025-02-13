from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser

from .models import Movie, Category
from .serializers import MovieListSerializer, MovieDetailSerializer, MovieSerializer, CategorySerializer
from .permission import IsAdminUserOrReadOnly
from utils.filters import MovieFilter

# Create your views here.
# method 1
"""@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        #movies = Movie.objects.all().values_list()
        movies = Movie.objects.filter(id__range=(2, 6))
        serializer = MovieListSerializer(movies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

    
"""class MovieDetail(APIView):
    def get(self, request, pk):
        try: 
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404

        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try: 
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404
        serializer = MovieDetailSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try: 
            movie = Movie.objects.get(pk=pk)
        except:
            raise Http404
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
    
"""class MovieDetail(mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""
        
## method 2
"""class MovieList(generics.ListCreateAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer"""
    
    
## method 3
class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]