# Generated by Django 4.0.1 on 2022-03-01 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0002_alter_shopdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopdata',
            name='Opentime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shopdata',
            name='closetime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='shopdata',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 19, 46, 40, 979684)),
        ),
    ]
