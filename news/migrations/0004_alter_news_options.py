# Generated by Django 4.0.5 on 2022-07-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_watch_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['title'], 'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
    ]