from django.conf import settings
from django.db import models
from django.utils import timezone

class Layout(models.Model):
    title = models.CharField(max_length=32)
    layout = models.TextField(blank=True)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=32)
    playlist = models.TextField(blank=True)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Station(models.Model):
    title = models.CharField(max_length=128)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Display(models.Model):
    title = models.CharField(max_length=32)
    layout = models.ForeignKey(Layout, related_name='dlayout', on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, related_name='dplaylist', on_delete=models.CASCADE)
    station = models.ForeignKey(Station, related_name='dstation', on_delete=models.CASCADE)
    enabled = models.BooleanField('Enabled',default=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Way(models.Model):
    title = models.CharField(max_length=128)
    station = models.ManyToManyField(Station)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Sched(models.Model):
    datetime = models.DateTimeField()
    way = models.ForeignKey(Way, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.datetime

