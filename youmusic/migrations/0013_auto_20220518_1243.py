# Generated by Django 3.2.10 on 2022-05-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youmusic', '0012_auto_20220518_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancion',
            name='cancion',
            field=models.FileField(default='files/audio', upload_to='static/youmusic/files'),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(default='files/img', upload_to='static/youmusic/files'),
        ),
    ]
