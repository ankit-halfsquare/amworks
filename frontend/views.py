from django.shortcuts import render

from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DeleteView, DetailView, View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse

from core.models import TestBuilding,TestBuildingItem
from core.api.serializers import TestBuildingSerializer

from .forms import BuildingForm,BuildingForm2,BuildingForm3





def sidebar(request):
    return render(request, 'frontend/sidebar.html')


def static_db(request):
    return render(request, 'frontend/table.html')


def main(request):
    return render(request, 'frontend/webix/new.html')

def add(request,pk=None):
    conntext={
        "pk":pk
    }
    return render(request, 'frontend/webix/addData2.html',conntext)






#============================================================
def home(request):
    return render(request, 'frontend/buildings.html')


def viewBuilding(request,pk):
    Building_obj = TestBuilding.objects.get(id=pk)
    serializer = TestBuildingSerializer(Building_obj)
   
    context = {"data":serializer.data}
    return render(request, 'frontend/building-details.html',context)


def updateBuilding(request,pk):
    Building_obj = TestBuilding.objects.get(id=pk)
    form = BuildingForm(instance=Building_obj)
    context = {"form":form}
    return render(request, 'frontend/building.html',context)

def addBuilding(request):
    form = BuildingForm()
    context = {"form":form}
    return render(request, 'frontend/building.html',context)



def addBuilding2(request):
    form = BuildingForm2()
    context = {"form":form}
    return render(request, 'frontend/building.html',context)

def addBuilding3(request):
    form = BuildingForm3()
    context = {"form":form}
    return render(request, 'frontend/building.html',context)



class BuildingView(FormView):
    form_class = BuildingForm
    template_name = 'frontend/building.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("valid==>")
        form.save()
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        print("Invalid==>")
        response = super().form_invalid(form)
        return response


   


