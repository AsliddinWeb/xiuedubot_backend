from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class UniversityInfo(models.Model):
    image = models.ImageField(upload_to='info/images')
    one_text = models.CharField(max_length=255)
    two_text = models.CharField(max_length=255)
    three_text = models.TextField()
    note = models.TextField()


    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Universitet haqida'

class Fakultet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='faculty')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Fakultetlar"

class Yonalish(models.Model):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='yonlaishlar')

    def __str__(self):
        return f"{self.title} | {self.fakultet.title}"

    class Meta:
        verbose_name_plural = "Yo'nalishlar"

class PhotoGallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Foto Galereya"

class VideoGallery(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='videos')
    youtube_link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Video Galereya"

class NewsCategory(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news-category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yangiliklar kategoriyasi"

class NewsArticle(models.Model):
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=455)
    body = RichTextField()
    image = models.ImageField(upload_to='news-images')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yangiliklar"