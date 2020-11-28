# Generated by Django 3.1.3 on 2020-11-28 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_reader_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='books',
            field=models.ManyToManyField(through='library.IssuingAInstance', to='library.Book'),
        ),
    ]
