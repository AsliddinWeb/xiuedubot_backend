# Generated by Django 4.2.5 on 2023-09-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0006_fakultet_newscategory_photogallery_videogallery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
