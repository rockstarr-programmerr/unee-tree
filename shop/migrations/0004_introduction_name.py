# Generated by Django 2.1 on 2018-08-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180829_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='introduction',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
