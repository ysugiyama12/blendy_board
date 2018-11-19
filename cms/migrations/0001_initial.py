# Generated by Django 2.1.3 on 2018-11-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='タイトル')),
                ('author', models.CharField(max_length=255, verbose_name='投稿者')),
                ('content', models.CharField(max_length=2000, verbose_name='本文')),
            ],
        ),
    ]
