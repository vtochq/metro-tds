# Generated by Django 2.2 on 2019-04-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tds', '0017_delete_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='display',
            name='station',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
    ]
