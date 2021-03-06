# Generated by Django 3.1.3 on 2020-11-28 16:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20201128_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='instanceofbook',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='instanceofbookinreadingroom',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='issuingainstance',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reader',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='readingroom',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='registers',
            name='owner',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='debit_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 413640, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_of_pub',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 413573, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='issuingainstance',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 414967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registers',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 416398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registers',
            name='unregister_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 416435, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registers',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 21, 14, 416420, tzinfo=utc)),
        ),
    ]
