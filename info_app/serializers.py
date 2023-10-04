from rest_framework import serializers

from .models import UniversityInfo, Fakultet, Yonalish, PhotoGallery, \
    VideoGallery, NewsCategory, NewsArticle

class UniversityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = "__all__"

class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = "__all__"

class YonalishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yonalish
        fields = "__all__"

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = "__all__"


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = "__all__"


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"


class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = "__all__"