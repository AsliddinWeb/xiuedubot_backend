# Generated by Django 4.2.5 on 2023-09-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_app', '0004_alter_universityinfo_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universityinfo',
            old_name='body',
            new_name='note',
        ),
        migrations.RemoveField(
            model_name='universityinfo',
            name='video',
        ),
        migrations.AddField(
            model_name='universityinfo',
            name='one_text',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='universityinfo',
            name='three_text',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='universityinfo',
            name='two_text',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
