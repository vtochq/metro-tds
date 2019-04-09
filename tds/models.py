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


class Display(models.Model):
    title = models.CharField(max_length=32)
    playlist = models.TextField(blank=True)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Station(models.Model):
    title = models.CharField(max_length=128)
    firstway_layout=models.ForeignKey(Layout, related_name='firstway_layout', on_delete=models.CASCADE)
    secondway_layout=models.ForeignKey(Layout, related_name='secondway_layout', on_delete=models.CASCADE)
    cashier_layout=models.ForeignKey(Layout, related_name='cashier_layout', on_delete=models.CASCADE)
    firstway_playlist=models.ForeignKey(Playlist, related_name='firstway_playlist', on_delete=models.CASCADE)
    secondway_playlist=models.ForeignKey(Playlist, related_name='secondway_playlist', on_delete=models.CASCADE)
    cashier_playlist=models.ForeignKey(Playlist, related_name='cashier_playlist', on_delete=models.CASCADE)
    enabled = models.BooleanField('Enabled',default=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
