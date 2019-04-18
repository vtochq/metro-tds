from django.urls import path, include
from . import views
from controlcenter.views import controlcenter

urlpatterns = [
    #path('admin_tools/', include('admin_tools.urls')),
    path('<int:pk>/', views.station_detail, name='station_detail'),
    path('<int:pk>/<int:disp>', views.display, name='display'),
    path('tdsapi/', views.Get_display_List.as_view()),
    path('home/', views.homepage),
    path('admin/dashboard/', controlcenter.urls),
]