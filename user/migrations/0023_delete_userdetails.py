# Generated by Django 3.2 on 2021-05-18 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_remove_channel_statistics_search_query'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
