# Generated by Django 2.1.1 on 2018-11-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181103_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
