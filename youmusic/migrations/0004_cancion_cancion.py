# Generated by Django 3.2.10 on 2022-05-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youmusic', '0003_imagen_nombreimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='cancion',
            field=models.FileField(default='audio', upload_to='audio'),
        ),
    ]
