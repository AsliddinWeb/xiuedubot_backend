from django.urls import path

from .views import UniversityInfoVS, FakultetVS, YonalishVS, \
    PhotoGalleryVS, VideoGalleryVS, NewsCategoryVS, NewsArticleVS, FakultetYonalishlariVS

urlpatterns = [
    path('university-info/', UniversityInfoVS.as_view()),
    path('fakultetlar/', FakultetVS.as_view()),
    path('fakultet/<int:faculty_id>/', FakultetYonalishlariVS.as_view()),
    path('yonalishlar/', YonalishVS.as_view()),
    path('foto-galereya/', PhotoGalleryVS.as_view()),
    path('video-galereya/', VideoGalleryVS.as_view()),
    path('news-category/', NewsCategoryVS.as_view()),
    path('news/', NewsArticleVS.as_view()),
]