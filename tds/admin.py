from django.contrib import admin
#from .models import Station, Layout, Playlist
from .models import *

admin.site.register(Station)
admin.site.register(Display)
admin.site.register(Layout)
admin.site.register(Playlist)
admin.site.register(Way)
admin.site.register(Sched)