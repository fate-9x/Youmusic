# Generated by Django 3.2.10 on 2022-05-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youmusic', '0005_auto_20220511_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='imagen',
            field=models.ImageField(default='files/img', upload_to='files/img'),
        ),
        migrations.DeleteModel(
            name='Imagen',
        ),
    ]
