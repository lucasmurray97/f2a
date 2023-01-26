# Generated by Django 4.1.4 on 2022-12-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('researcher', '0001_initial'),
        ('paper', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='tools', to='researcher.researcher')),
                ('paper', models.ManyToManyField(blank=True, related_name='tools', to='paper.paper')),
                ('projects', models.ManyToManyField(blank=True, related_name='tools', to='project.project')),
            ],
        ),
    ]
