from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.station_detail, name='station_detail'),
    path('<int:pk>/<int:disp>', views.display, name='display'),
]