# Generated by Django 2.0 on 2017-12-18 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171218_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 18, 16, 50, 46, 970840, tzinfo=utc)),
        ),
    ]
