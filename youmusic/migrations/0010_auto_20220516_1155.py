# Generated by Django 3.2.10 on 2022-05-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youmusic', '0009_auto_20220516_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='cancion',
            field=models.FileField(default='files/audio', upload_to='files/audio'),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(default='files/img', upload_to='files/img'),
        ),
    ]
