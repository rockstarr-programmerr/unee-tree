# Generated by Django 2.1.1 on 2018-11-30 14:13

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0008_auto_20181112_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='color_1',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18),
        ),
        migrations.AlterField(
            model_name='banner',
            name='color_2',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18),
        ),
        migrations.AlterField(
            model_name='banner',
            name='color_3',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18),
        ),
        migrations.AlterField(
            model_name='banner',
            name='color_4',
            field=colorfield.fields.ColorField(blank=True, default='#ffffff', max_length=18),
        ),
    ]
