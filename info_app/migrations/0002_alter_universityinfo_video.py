# Generated by Django 4.2.5 on 2023-09-10 09:22

from django.db import migrations, models
import info_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityinfo',
            name='video',
            field=models.FileField(upload_to='info/videos', validators=[info_app.validators.validate_file_extension]),
        ),
    ]
