# Generated by Django 2.1.1 on 2018-11-10 16:09

from django.db import migrations, models
import introduction.models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0006_auto_20181110_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to=introduction.models.upload_image_path, verbose_name='Ảnh'),
        ),
    ]
