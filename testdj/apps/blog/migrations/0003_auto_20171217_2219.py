# Generated by Django 2.0 on 2017-12-17 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171217_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(blank=True, max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='country',
            field=models.CharField(blank=True, max_length=130, null=True),
        ),
    ]
