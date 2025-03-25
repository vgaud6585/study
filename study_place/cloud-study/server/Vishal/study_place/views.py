from django.shortcuts import render,redirect, get_object_or_404
from .forms import StudyForm
from .models import StudyRecords
# Create your views here.

def home(request):
  StuRec = StudyRecords.objects.all()
  print(StuRec) 
  print(type(StuRec)) 
  dt = {
    "nm":"Vishal Gaud",
    "stur":StuRec,
  }
  pt = "studyPlace/html/home.html"
  return render(request, pt, dt)
 
  
def add(request):
  if request.method == 'POST':
    form = StudyForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = StudyForm()
  pt = "studyPlace/html/addDetail.html"
  dt = {
    "nm":"Vishal Gaud",
    #form:"form",
    "form":form,
  }
  return render(request, pt, dt)
  
def sturec_edit(request, pk):
  stur = get_object_or_404(StudyRecords, pk=pk)
  if request.method == 'POST':
    form = StudyForm(request.POST, request.FILES, instance=stur)
    print('ins\n\n')
    #print(instance)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    #form = StudyForm(instance=stur)
    form = StudyForm(instance=stur)
  pt = "studyPlace/html/addDetail.html"
  return render(request, pt, {'stur': form})
  

def last_item(request):
  StuRec = StudyRecords.objects.last()
  dt = {
    "status" : "last record",
    "sturec" : StuRec,
  }
  pt = "studyPlace/html/detail.html"
  return render(request, pt, dt)
  
def find_item(request):
  obj = None
  if request.method == "POST":
    get_value = int(request.POST.get("get_id"))
    obj = get_object_or_404(StudyRecords, pk=get_value)
    #pt = "studyPlace/html/detail.html"
    # dt = {
    #   "sturec": obj,
    # }
    #return render(request, pt, dt)
  pt = "studyPlace/html/find.html"
  dt = {
    "sturec": obj,
  }
  return render(request, pt, dt)