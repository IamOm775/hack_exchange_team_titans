# Generated by Django 3.1.7 on 2021-05-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_extendeduser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='channel_logo',
            field=models.ImageField(default=None, upload_to='user/channel_logo'),
        ),
    ]