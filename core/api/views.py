from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
from core.models import Project,Building
from .serializers import *


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.db import connection

def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)



    
class ProjectView(APIView):
    
    def get(self, request,pk=None, *args, **kwargs):
        Project_obj = Project.objects.all()
        serializer = ProjectSerializer(Project_obj, many =True)
        return Response({ "data":serializer.data})

    
    def post(self, request,pk=None, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data  
            val =[]
            for k,v in data.items():
                val.append(v)
            query = f''' INSERT INTO project (name, company_id) VALUES {tuple(val)}; '''
                                
            print(query)
            query = query.replace("None","")
            my_custom_sql(query)
            # serializer.save()
            return Response({"message": " Record has been added", "data": serializer.data},status=status.HTTP_201_CREATED)
        return Response({"message": " Record has been not added"})

    
    def put(self, request, pk=None, *args, **kwargs):
        id = pk
        serializer = ProjectSerializer(data=request.data)

        # obj = Project.objects.get(id=id)
        # serializer = ProjectSerializer(obj,data=request.data)
        if serializer.is_valid():
            data = serializer.data 
            print(data)
            raw = ''
            for k,v in data.items():
                if k != 'id':
                    raw = raw + k + '=' +  "'" + str(v) + "'" + ' ,'

            query = f''' UPDATE  project SET {raw[:-1]} WHERE id = id ; '''  
            print(query)     
            my_custom_sql(query)
            # serializer.save()
            return Response({"message": " Record has been updated", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"message": " Record has not updated", "data": serializer.data})


    
    def delete(self, request, pk=None, *args, **kwargs):
        id = pk
        obj = Project.objects.get(id=id)
        obj.delete()
        return Response({ "message": " Record has been deleted"},status=status.HTTP_204_NO_CONTENT) 



class BuildingView(APIView):
    
    def get(self, request,pk=None, *args, **kwargs):
        Project_obj = Building.objects.all()
        serializer = BuildingSerializer(Project_obj, many =True)
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