# Generated by Django 2.2 on 2019-04-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tds', '0020_auto_20190409_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
    ]