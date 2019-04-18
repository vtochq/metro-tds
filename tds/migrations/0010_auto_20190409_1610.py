# Generated by Django 2.2 on 2019-04-09 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tds', '0009_auto_20190409_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='display',
            name='stationq',
        ),
        migrations.AddField(
            model_name='display',
            name='stationa',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='tds.Station'),
            preserve_default=False,
        ),
    ]
