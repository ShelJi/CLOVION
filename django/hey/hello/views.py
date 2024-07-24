from django.shortcuts import render, redirect
from hello.forms import Wow_form
from hello.models import Wow_model

# Create your views here.
def indexPage(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        data = Wow_form(request.POST, request.FILES)
        
        if data.is_valid():
            data.save()
            return redirect("/display/")
        
    return render(request, "index.html")

def displayPage(request):
    values = Wow_model.objects.all()
    context = {"value" : values}
    return render(request, "display.html", context)

def displayDelete(request, id):
    data = Wow_model.objects.get(id = id)
    data.delete()
    
    return redirect("/display/")

def displayEdit(request, id):
    data = Wow_model.objects.get(id = id)
    context = {"dataEdit": data}
    
    if request.method == 'POST':
        value = Wow_form(request.POST, request.FILES, instance = data)
        if value.is_valid():
            data.save()
            return redirect("/display/")
    
    return render(request, "edit.html", context)
