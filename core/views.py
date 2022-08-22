from django.shortcuts import render,HttpResponse
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.


def index(request):
    return HttpResponse("Hello World")