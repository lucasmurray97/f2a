# Generated by Django 4.1.4 on 2023-09-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='event',
            field=models.BooleanField(default=False),
        ),
    ]
