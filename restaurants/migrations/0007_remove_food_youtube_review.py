# Generated by Django 3.0.7 on 2020-07-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_foodreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='youtube_review',
        ),
    ]
