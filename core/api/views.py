from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from core.models import Project,Building,Test
from .serializers import *


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.db import connection

def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)



    
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
            Building_obj = Project.objects.get(id=id)
            serializer = BuildingSerializer(Building_obj)
        else:
            Building_obj = Project.objects.all()
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




class TestView(APIView):
    
    def get(self, request,pk=None, *args, **kwargs):
        id = pk
        if id:
            Test_obj = Project.objects.get(id=id)
            serializer = TestSerializer(Test_obj)
        else:
            Test_obj = Test.objects.all()
            serializer = TestSerializer(Test_obj, many =True)
        return Response({ "data":serializer.data})


    
    def post(self, request,pk=None, *args, **kwargs):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been added", "data": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message": " Record has been not added"})


    
    def put(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Test.objects.get(id=id)
        serializer = TestSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": " Record has been updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": " Record has not updated", "data": serializer.data})

    
    def delete(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Test.objects.get(id=id)
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