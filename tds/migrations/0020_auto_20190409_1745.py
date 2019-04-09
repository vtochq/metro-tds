# Generated by Django 2.2 on 2019-04-09 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tds', '0019_auto_20190409_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sched',
            name='title',
        ),
        migrations.RemoveField(
            model_name='station',
            name='enabled',
        ),
        migrations.AddField(
            model_name='sched',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sched',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tds.Station'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tds.Station')),
            ],
        ),
        migrations.AddField(
            model_name='sched',
            name='way',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tds.Way'),
            preserve_default=False,
        ),
    ]