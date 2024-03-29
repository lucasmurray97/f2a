# Generated by Django 4.1.4 on 2023-10-03 12:11

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0018_alter_researcher_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, quality=0, scale=None, size=[150, 180], upload_to='img/researchers/'),
        ),
    ]
