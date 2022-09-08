from django.urls import include, path, re_path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('webix/', views.main, name='main'),
   path('webix/add/', views.add, name='add'),
   path('webix/update/<int:pk>', views.add, name='update'),
   path('webix/sidebar/', views.sidebar, name='sidebar'),


   path('loader/', views.loader, name='loader'),

<<<<<<< HEAD
=======
   path('webix/form/', views.form, name='form'),



>>>>>>> 7524f6ffba12a71dbc1f47eb0fd044b3eaeb0ad1
   path('building/', views.addBuilding, name='building'),
   path('building2/', views.addBuilding2, name='building2'),
   path('building3/', views.addBuilding3, name='building3'),


   path('building/update/<int:pk>', views.updateBuilding, name='update-building'),
   path('building/<int:pk>', views.viewBuilding, name='view-building'),
   path('', views.home, name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 