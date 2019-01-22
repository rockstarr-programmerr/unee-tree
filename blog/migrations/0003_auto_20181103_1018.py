# Generated by Django 2.1.1 on 2018-11-03 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181031_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterIndexTogether(
            name='blogpost',
            index_together=set(),
        ),
    ]