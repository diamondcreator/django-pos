# Generated by Django 2.1 on 2018-09-08 09:49

from django.db import migrations, models
import pos.models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_auto_20180811_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(null=True, upload_to=pos.models.cutomer_photo_directory),
        ),
    ]
