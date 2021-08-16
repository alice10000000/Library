# Generated by Django 2.2.10 on 2021-08-10 19:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20210809_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowrecord',
            old_name='updated_by',
            new_name='closed_by',
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 19, 8, 34, 95437, tzinfo=utc)),
        ),
    ]