# Generated by Django 2.1.1 on 2018-11-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181110_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='hashtag',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
