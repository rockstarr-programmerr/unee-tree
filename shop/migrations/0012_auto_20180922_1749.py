# Generated by Django 2.1.1 on 2018-09-22 10:49

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180922_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=shop.models.upload_image_path),
        ),
    ]
