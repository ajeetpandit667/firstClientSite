from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
  return render(request,"home.html")

def contactPage(request):
  return render(request,"contact.html")

def servicePage(request):
  return render(request,"service.html")

def gallary(request):
  return render(request,"gallary.html")

def aboutPage(request):
  return render(request,"about.html")