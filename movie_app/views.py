from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, ReviewSerializer, MovieSerializer


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         queryset = Movie.objects.all()
#         serializer = MovieSerializer(queryset, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)

class ReviewDetailAPIview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, id):
#     queryset = get_object_or_404(Movie, id=id)
#     if request.method == 'GET':
#         queryset = get_object_or_404(Movie, id=id)
#         serializer = MovieSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(queryset, data=request.data, instance=get_object_or_404(Movie, id=id))
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class MovieAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class MovieDetailAPIview(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, id):
#     queryset = get_object_or_404(Review, id=id)
#     if request.method == 'GET':
#         queryset = get_object_or_404(Review, id=id)
#         serializer = ReviewSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#     elif request.method == 'PUT':
#         serializer = ReviewSerializer(queryset, data=request.data, instance=get_object_or_404(Review, id=id))
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class ReviewAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'




# @api_view(['GET', 'PUT'])
# def director_list(request):
#     if request.method == 'GET':
#         queryset = Director.objects.all()
#         serializer = DirectorSerializer(queryset, many=True)
#         return Response(serializer.data, status=200)
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(data=request.data)
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)


class DirectorDetailAPIview(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer



# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail(request, id):
#     queryset = get_object_or_404(Director, id=id)
#     if request.method == 'GET':
#         queryset = get_object_or_404(Director, id=id)
#         serializer = DirectorSerializer(queryset, many=False)
#         return Response(serializer.data, status=200)
#     elif request.method == 'PUT':
#         serializer = DirectorSerializer(queryset, data=request.data, instance=get_object_or_404(Director, id=id))
#         serializer.is_valid(raise_exceptions=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=204)

class DirectorAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


