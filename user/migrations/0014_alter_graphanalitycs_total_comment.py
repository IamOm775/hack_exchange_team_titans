# Generated by Django 3.2 on 2021-05-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20210514_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphanalitycs',
            name='total_comment',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
