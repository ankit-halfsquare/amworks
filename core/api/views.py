from rest_framework.views import APIView 
from rest_framework import status,generics
from rest_framework.response import Response
from core.models import Project,Building,BuildingItem,Organization,TestBuilding,TestBuildingItem
from .serializers import *


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

import uuid



# People tables API Views====================================People tables API Views================================================People tables API Views
#

class PeopleListCreateAPIView(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    # def perform_create(self, serializer): # optional if need any modification before save data
    #     pass
        # user=self.request.user
        # title = serializer.validated_data.get('title')
        # serializer.save(user=suser,title=title)
        # serializer.save()


class PeopleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_feild = 'pk'


class PeopleUpdateAPIView(generics.UpdateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_feild = 'pk'

    # def perform_update(self, serializer): # optional if need any modification before
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content') or None
    #     if content is None: 
    #             content = title
    #     instance = serializer.save(content=content)


class PeopleDestroyAPIView(generics.DestroyAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    lookup_field = 'pk'



# Project tables API Views====================================Project tables API Views================================================Project tables API Views
#


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

class ProjectUpdateAPIView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'pk'

class ProjectDestroyAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Building tables API Views====================================Building tables API Views================================================Building tables API Views
#

class BuildingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'pk'

class BuildingUpdateAPIView(generics.UpdateAPIView): 
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = 'pk'

class BuildingDestroyAPIView(generics.DestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# Organization tables API Views====================================Organization tables API Views================================================Organization tables API Views
#
class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'pk'

class OrganizationUpdateAPIView(generics.UpdateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'pk'

class OrganizationDestroyAPIView(generics.DestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


# BuildingItem tables API Views====================================BuildingItem tables API Views================================================BuildingItem tables API Views
#
class BuildingItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = BuildingItem.objects.all()
    serializer_class = BuildingItemSerializer

class BuildingItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = BuildingItem.objects.all()
    serializer_class = BuildingItemSerializer
    lookup_field = 'pk'

class BuildingItemUpdateAPIView(generics.UpdateAPIView):
    queryset = BuildingItem.objects.all()
    serializer_class = BuildingItemSerializer
    lookup_field = 'pk'

class BuildingItemDestroyAPIView(generics.DestroyAPIView):
    queryset = BuildingItem.objects.all()
    serializer_class = BuildingItemSerializer



# Building tables API Views====================================Building tables API Views================================================Building tables API Views
#

class TestBuildingListCreateAPIView(generics.ListCreateAPIView):
    queryset = TestBuilding.objects.all()
    serializer_class = TestBuildingSerializer

class TestBuildingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TestBuilding.objects.all()
    serializer_class = TestBuildingSerializer
    lookup_field = 'pk'

class TestBuildingUpdateAPIView(generics.UpdateAPIView):
    queryset = TestBuilding.objects.all()
    serializer_class = TestBuildingSerializer
    lookup_field = 'pk'

class TestBuildingDestroyAPIView(generics.DestroyAPIView):
    queryset = TestBuilding.objects.all()
    serializer_class = TestBuildingSerializer


# TestBuildingItem tables API Views====================================TestBuildingItem tables API Views================================================TestBuildingItem tables API Views
#
class TestBuildingItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = TestBuildingItem.objects.all()
    serializer_class = TestBuildingItemSerializer

class TestBuildingItemRetrieveAPIView(generics.RetrieveAPIView):
    queryset = TestBuildingItem.objects.all()
    serializer_class = TestBuildingItemSerializer
    lookup_field = 'pk'

class TestBuildingItemUpdateAPIView(generics.UpdateAPIView):
    queryset = TestBuildingItem.objects.all()
    serializer_class = TestBuildingItemSerializer
    lookup_field = 'pk'

class TestBuildingItemDestroyAPIView(generics.DestroyAPIView):
    queryset = TestBuildingItem.objects.all()
    serializer_class = TestBuildingItemSerializer

# End tables API Views==================================== End tables API Views================================================ End tables API Views
#
#
#
#
#

# Old Stuff====================================Old Stuff================================================Old Stuff
#
#
#
#
#
#


class ProjectView(APIView):
    
    def get(self, request,pk=None, *args, **kwargs):
        id = pk
        if id:
            Project_obj = Project.objects.get(id=id)
            serializer = ProjectSerializer(Project_obj)
        else:
            Project_obj = Project.objects.all()
            serializer = ProjectSerializer(Project_obj, many =True)
        return Response({ "data":serializer.data})

    
    def post(self, request,pk=None, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been added", "data": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message": " Record has been not added"})
    
    def put(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Project.objects.get(id=id)
        serializer = ProjectSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": " Record has not updated", "data": serializer.data})


    
    def delete(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Project.objects.get(id=id)
        obj.delete()
        return Response({ "message": " Record has been deleted"},status=status.HTTP_204_NO_CONTENT) 



class BuildingView(APIView):
    def get(self, request,pk=None, *args, **kwargs):
        id = pk 
        if id:
            Building_obj = Building.objects.get(id=id)
            serializer = BuildingSerializer(Building_obj)
        else:
            Building_obj = Building.objects.all()
            serializer = BuildingSerializer(Building_obj, many =True)
        
        return Response({ "data":serializer.data})


    
    def post(self, request,pk=None, *args, **kwargs):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been added", "data": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message": " Record has been not added"})


    
    def put(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Building.objects.get(id=id)
        serializer = BuildingSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": " Record has not updated", "data": serializer.data})

    
    def delete(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Building.objects.get(id=id)
        obj.delete()
        return Response({ "message": " Record has been deleted"},status=status.HTTP_204_NO_CONTENT) 



# @api_view(('PUT','DELETE'))
# @csrf_exempt
# def project(request,pk):
#     id = pk
#     obj = Project.objects.get(id=id)
#     if request.method =='PUT':
#         serializer = ProjectSerializer(obj,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": " Record has been updated", "data": serializer.data}, status=status.HTTP_200_OK)
#         return Response({"message": " Record has not updated", "data": serializer.data})
    
#     obj.delete()
#     return Response({ "message": " Record has been deleted"},status=status.HTTP_204_NO_CONTENT) 