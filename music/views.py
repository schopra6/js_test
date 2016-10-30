from django.shortcuts import render
from django.http import HttpResponse

from .models import album
# Create your views here.
def index(request):
  return render(request,'music/index.html')

def detail(request,album_id):
    return render(request,'music/detail.html',{'album_id':album_id})