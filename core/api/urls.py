from django.urls import path   
from . import views

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    
    # project urls==================================== project urls================================================ project urls
    #
    path("project/", views.ProjectListCreateAPIView.as_view(), name = "ProjectListCreateAPIView"),
    path("project/<int:pk>/", views.ProjectRetrieveAPIView.as_view(), name = "ProjectRetrieveAPIView"),
    path("project/update/<int:pk>/", views.ProjectUpdateAPIView.as_view(), name = "ProjectUpdateAPIView"),
    path("project/delete/<int:pk>/", views.ProjectDestroyAPIView.as_view(), name = "ProjectDestroyAPIView"),

    # building urls==================================== building urls================================================ building urls
    #
    path("building/", views.BuildingListCreateAPIView.as_view(), name = "BuildingListCreateAPIView"),
    path("building/<int:pk>/", views.BuildingRetrieveAPIView.as_view(), name = "BuildingRetrieveAPIView"),
    path("building/update/<int:pk>/", views.BuildingUpdateAPIView.as_view(), name = "BuildingUpdateAPIView"),
    path("building/delete/<int:pk>/", views.BuildingDestroyAPIView.as_view(), name = "BuildingDestroyAPIView"),

    # building-item urls==================================== building-item urls================================================ building-item urls
    #
    path("building-item/", views.BuildingItemListCreateAPIView.as_view(), name = "BuildingItemListCreateAPIView"),
    path("building-item/<int:pk>/", views.BuildingItemRetrieveAPIView.as_view(), name = "BuildingItemRetrieveAPIView"),
    path("building-item/update/<int:pk>/", views.BuildingItemUpdateAPIView.as_view(), name = "BuildingItemUpdateAPIView"),
    path("building-item/delete/<int:pk>/", views.BuildingItemDestroyAPIView.as_view(), name = "BuildingItemDestroyAPIView"),

    # people urls==================================== people urls================================================ people urls
    #
    path("people/", views.PeopleListCreateAPIView.as_view(), name = "PeopleListCreateAPIView"),
    path("people/<int:pk>/", views.PeopleRetrieveAPIView.as_view(), name = "PeopleRetrieveAPIView"),
    path("people/update/<int:pk>/", views.PeopleUpdateAPIView.as_view(), name = "PeopleUpdateAPIView"),
    path("people/delete/<int:pk>/", views.PeopleDestroyAPIView.as_view(), name = "PeopleDestroyAPIView"),


    # organization urls==================================== organization urls================================================ organization urls
    #
    path("organization/", views.OrganizationListCreateAPIView.as_view(), name = "OrganizationListCreateAPIView"),
    path("organization/<int:pk>/", views.OrganizationRetrieveAPIView.as_view(), name = "OrganizationRetrieveAPIView"),
    path("organization/update/<int:pk>/", views.OrganizationUpdateAPIView.as_view(), name = "OrganizationUpdateAPIView"),
    path("organization/delete/<int:pk>/", views.OrganizationDestroyAPIView.as_view(), name = "OrganizationDestroyAPIView"),

    

   

]

