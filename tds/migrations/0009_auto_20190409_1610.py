# Generated by Django 2.2 on 2019-04-09 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tds', '0008_auto_20190409_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='display',
            old_name='station',
            new_name='stationq',
        ),
    ]
