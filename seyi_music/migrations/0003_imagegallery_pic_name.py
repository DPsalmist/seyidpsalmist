# Generated by Django 2.2.2 on 2020-04-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seyi_music', '0002_auto_20200403_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='pic_name',
            field=models.CharField(default='My Pic', max_length=50),
        ),
    ]
