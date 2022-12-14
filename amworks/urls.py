
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('core/api/', include('core.api.urls')),
    path('', include('frontend.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
