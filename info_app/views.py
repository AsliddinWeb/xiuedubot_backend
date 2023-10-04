from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import UniversityInfo, Fakultet, Yonalish, PhotoGallery, \
    VideoGallery, NewsCategory, NewsArticle
from .serializers import UniversityInfoSerializer, FakultetSerializer, \
    YonalishSerializer, PhotoGallerySerializer, VideoGallerySerializer, \
    NewsCategorySerializer, NewsArticleSerializer


class UniversityInfoVS(generics.ListAPIView):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversityInfoSerializer


class FakultetVS(generics.ListAPIView):
    queryset = Fakultet.objects.all()
    serializer_class = FakultetSerializer

class FakultetYonalishlariVS(generics.ListAPIView):
    queryset = Yonalish.objects.all()
    serializer_class = FakultetSerializer

    def get_queryset(self):
        faculty_id = self.kwargs['faculty_id']
        return Yonalish.objects.filter(fakultet=faculty_id)

class YonalishVS(generics.ListAPIView):
    queryset = Yonalish.objects.all()
    serializer_class = FakultetSerializer


class PhotoGalleryVS(generics.ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

class VideoGalleryVS(generics.ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer

class NewsCategoryVS(generics.ListAPIView):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer

class NewsArticleVS(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer