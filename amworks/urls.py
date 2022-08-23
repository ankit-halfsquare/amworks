
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('core/api/', include('core.api.urls')),
    path('admin', admin.site.urls),
    path('', include('frontend.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
