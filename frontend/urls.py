from django.urls import include, path, re_path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('table', views.static_db, name='static_db_example'),
   path('', views.sidebar, name='webix'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)