from django.urls import path   
from . import views

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
   
    path("project/", views.ProjectView.as_view(), name = "project"),
    path("project/<int:pk>/", views.ProjectView.as_view(), name = "updateDeleteProject"),
    path("building/", views.BuildingView.as_view(), name = "building"),
    path("building/<int:pk>/", views.ProjectView.as_view(), name = "updateDeleteBuilding"),

]


# urlpatterns = [
   
#     path("project/<int:pk>", views.project, name = "updateDeleteProject"),
#     path("project/", views.ProjectView.as_view(), name = "project"),
   
# ]