# Generated by Django 2.1.1 on 2018-09-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180922_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='usage',
            field=models.CharField(blank=True, max_length=100, verbose_name='Công dụng'),
        ),
    ]