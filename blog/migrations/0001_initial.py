# Generated by Django 3.1.2 on 2020-11-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tag')),
            ],
        ),
    ]