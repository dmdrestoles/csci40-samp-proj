# Generated by Django 5.0.2 on 2024-02-28 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=31)),
                ('descn', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('namespace', models.CharField(max_length=255)),
                ('entry', models.TextField()),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wiki.articlecategory')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]