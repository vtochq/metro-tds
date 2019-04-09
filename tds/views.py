from django.shortcuts import render, get_object_or_404, redirect
from .models import Station
from django.template import Engine


# Create your views here.

def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    return render(request, 'tds/station_detail.html', {'station': station})

def display(request, pk, disp):
    station = get_object_or_404(Station, pk=pk)
    layout='{{ layout }}'
    template = Engine().from_string(layout)
    return template.render
    #return render(request, 'tds/display.html', {'layout': layout})