from django.contrib import admin
#from .models import Station, Layout, Playlist
from .models import *
#from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.utils.encoding import force_text
#import pdb;

class StationAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')


class SchedStationFilter(admin.SimpleListFilter):
    title = 'Stations'
    parameter_name = 'station__id__exact'
    
    def lookups(self, request, model_admin):
        stations = Station.objects.all()
        return [(c.id, c.title) for c in stations]
        
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(station__id__exact=self.value())
        else:
            return queryset.filter(station__id__exact=1)
    
    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == force_text(lookup) or (self.value() is None and force_text(lookup) == '1'),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, remove='way__id__exact'),
                'display': title,
            }

class SchedWayFilter(admin.SimpleListFilter):
    title = 'Ways'
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'way__id__exact'
    
    def lookups(self, request, model_admin):
        #ways = set([c.way for c in model_admin.model.objects.all()])
        if 'station__id__exact' in request.GET:
            station_id=request.GET['station__id__exact']
        else:
            station_id=1
        
        ways = Way.objects.filter(station__id__exact=station_id)
        #query_attrs = dict([(param, val) for param, val in request.GET.items()])
        #ways = ways.filter(station__id__exact=request.GET['station__id__exact'])
        
        return [(c.id, c.title) for c in ways]
        '''
        qs = model_admin.get_queryset(request)
        query_attrs = dict([(param, val) for param, val in request.GET.items()])
        qs = qs.filter(**query_attrs)
        ret=[]
        for book in qs:  # or might be able to use yeild here
            ret.append((book.way_id, book.way))
        return ret
        '''

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(way__id__exact=self.value())
        else:
            return queryset


class SchedAdmin(admin.ModelAdmin):
    list_display = ('time', 'way', 'station', 'enabled')
    list_filter = (SchedStationFilter, SchedWayFilter)

@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    #search_fields = ('title',)
    list_filter = ('title',)
    list_display = ('title', 'station','enabled',)
    #list_filter = (StationListFilter,'title')

    

admin.site.register(Station, StationAdmin)
#admin.site.register(Display, DisplayAdmin)
admin.site.register(Layout)
admin.site.register(Playlist)
admin.site.register(Way)
admin.site.register(Sched, SchedAdmin)
