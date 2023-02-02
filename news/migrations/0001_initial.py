# Generated by Django 4.1.4 on 2022-12-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research', '0001_initial'),
        ('researcher', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=300)),
                ('link', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='photos/news/')),
                ('mentioned', models.ManyToManyField(blank=True, related_name='news', to='researcher.researcher')),
                ('projects', models.ManyToManyField(blank=True, related_name='news', to='project.project')),
                ('related_news', models.ManyToManyField(blank=True, to='news.news')),
                ('research_lines', models.ManyToManyField(blank=True, related_name='news', to='research.research')),
            ],
        ),
    ]