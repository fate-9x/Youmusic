# Generated by Django 3.2.10 on 2022-05-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youmusic', '0011_auto_20220518_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='cancion',
            field=models.FileField(default='files/audio', upload_to='files/audio'),
        ),
        migrations.AddField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(default='files/img', upload_to='files/img'),
        ),
    ]
