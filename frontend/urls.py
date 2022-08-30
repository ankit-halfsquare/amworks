from django.urls import include, path, re_path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('table/', views.static_db, name='static_db_example'),
   path('sidebar/', views.sidebar, name='sidebar'),
   path('building/', views.addBuilding, name='building'),
   path('building/update/<int:pk>', views.updateBuilding, name='update-building'),
   path('building/<int:pk>', views.viewBuilding, name='view-building'),
   path('', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)