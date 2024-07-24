from django.shortcuts import render, redirect
from ginger.forms import employeeDataForm
from ginger.forms import LoginCheck
from ginger.models import employeeData

def loginPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if employeeData.objects.filter(name = name, password = password).exists():
            return redirect("/display/")

    return render(request,"login/login_1.html")

def addUser(request):
    if request.method == 'POST':
        newUser = LoginCheck(request.POST)
        newUser.save()
        return redirect("/login/")
    
    return render(request, "addUser.html")

def changePass(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if employeeData.objects.filter(name = name).exists():
            data = employeeData.objects.get(name = name)
            changedData = LoginCheck(request.POST, instance = data)
            if changedData.is_valid():
                data.save()
                return redirect("/login/")
    return render(request, "changePass.html")
    
def updatePage(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        data = employeeDataForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return redirect("/display/")
    return render(request, "update/update.html")

def displayPage(request):
    content = employeeData.objects.all()
    values = {"value": content}
    return render(request, "display/display.html", values)

def editButton(request, id):
    data = employeeData.objects.get(id = id)
    values = {"value" : data}
    print(request.POST)
    print(request.FILES)

    if request.method == 'POST':
        editedData = employeeDataForm(request.POST, request.FILES, instance= data)
        if editedData.is_valid():
            data.save()
            return redirect("/display/")
    
    return render(request, "edit/edit.html", values)
    
def deleteButton(request, id):
    data = employeeData.objects.get(id = id)
    data.delete()
    return redirect("/display/")