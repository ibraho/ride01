from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import *

def book(request):
  form=ConForm(request.POST)
  if request.method=='POST':
    if form.is_valid():
      form=ConForm(request.POST)
      form.save()
      form=ConForm()
      return redirect(reverse('index'))

  else:
    form=ConForm(request.POST)

  return render(request,'index.html',{'form': form} )

def index(request):
  form=ConForm(request.POST)

  return render(request,'index.html',{'form': form} )