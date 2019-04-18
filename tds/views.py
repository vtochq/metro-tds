from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import displaySerializer

# Create your views here.

def station_detail(request, pk):
    station = get_object_or_404(Station, pk=pk)
    return render(request, 'tds/station_detail.html', {'station': station})

def display(request, pk, disp):
    station = get_object_or_404(Station, pk=pk)
    
    layout='{{ layout }}'

    playlist=station.firstway_playlist.playlist


    data = {
        'title': station.title,
        'layout': layout,
        'playlist': playlist,
    }
    #template = Engine().from_string(layout)
    return JsonResponse(data)
    #return render(request, 'tds/display.html', {'layout': layout})

class Get_display_List(APIView):
    def get(self, request):
        display = Display.objects.all()
        serialized = displaySerializer(display, many=True)
        return Response(serialized.data)
    
def homepage(request):
    return render(request, 'index.html')
