from django.shortcuts import render

def home_page(request):
  pt = "base.html"
  dt = {
    
  }
  return render(request, pt, dt)