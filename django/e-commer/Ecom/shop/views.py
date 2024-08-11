from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from shop.forms import *
from shop.models import *

# home
def home(request):
    if request.session:
        usersigned = request.session.get('buyer', None)
        
    trending = ProductData.objects.filter(trending=True)
    return render(request, 'index.html', {"usersigned": usersigned,
                                          "trending":trending})

def emptyRedirect(request, empty):
    return redirect(reverse('shop:home'))
def empty(request):
    return redirect(reverse('shop:home'))

# buyer login
def login(request):
    userLoggedin = ""
    
    if request.method == 'POST':
        name = request.POST.get("name")
        
        if buyerData.objects.filter(name = name).exists():
            password = request.POST.get("password")
            
            if buyerData.objects.filter(name = name, password = password).exists():
                userLoggedin = "exists"#################################################
                request.session['buyer'] = name
                return redirect(reverse("shop:home"))
            else:
                userLoggedin = "Incorrect Password"
                
        else:
            userLoggedin = "User does not Exists"
            
    return render(request, "login.html", {"topic": "login",
                                          "userLoggedin": userLoggedin})

def register(request):
    userLoggedin = ""
    if request.method == 'POST':
        user = BuyerDataForm(request.POST)
        if user.is_valid():
            name = request.POST.get("name")
            if buyerData.objects.filter(name = name).exists():
                userLoggedin = "User already exists"
            else:
                user.save()
                return redirect(reverse("shop:login"))
        else:
            userLoggedin="Enter valid details"
    return render(request, "login.html", {"topic": "new user",
                                          "userLoggedin": userLoggedin})

# buyer profile
def userProfile(request):
    usersigned = request.session.get('buyer', None)
    if request.method == 'POST':
        if 'logout' in request.POST:
            request.session.flush()
            return redirect(reverse("shop:home"))
    return render(request, "userProfile.html", {"usersigned": usersigned})

# seller
# seller login 
def sellerLogin(request):
    userLoggedin = ""
    
    if request.method == 'POST':
        name = request.POST.get("name")
        print(name)
        if UserData.objects.filter(name = name).exists():
            password = request.POST.get("password")
            name = request.POST.get("name")

            print(password)
            # if (request.POST["name"] == name and request.POST["password"]== password):
                
            if UserData.objects.filter(name = name, password = password).exists():
                id_val = UserData.objects.get(name = name, password = password)
                id_v = id_val.id
                return redirect(reverse('shop:sellerProfile', args=[id_v]))
            else:
                userLoggedin = "Incorrect Password"
                                
        else:
            userLoggedin = "User does not exists"
            
        
    return render(request, "login.html", {"topic": "seller login", 
                                          "userLoggedin": userLoggedin})

def newseller(request):
    userLoggedin = ""
    if request.method == 'POST':
        newUser = UserDataForm(request.POST)
        name = request.POST.get('name')
        
        if newUser.is_valid():
            
            if UserData.objects.filter(name = name).exists():
                userLoggedin = "User already exist"
            else:
                newUser.save()
                return redirect(reverse('shop:seller'))
            
        else:
            userLoggedin="Enter valid details"
        
    return render(request, "login.html", {"topic": "seller register",
                                          "userLoggedin": userLoggedin})

# seller product update
def seller(request, id):
    usersigned = ""
    signedUser = UserData.objects.get(id = id)
    usersigned = signedUser.name
    id = id
    if request.method == 'POST':
        form = ProductDataForm(request.POST, request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.user = signedUser
            product.save()
            
            return redirect(reverse('shop:sellerProfile', args=[id] ))
        
    return render(request, "sellerPage.html", {"usersigned": usersigned,
                                               "id": id})

# seller profile
def profile(request, id):
    usersigned = ""
    id = id
    signedUser = UserData.objects.get(id = id)
    usersigned = signedUser.name
    details = signedUser.productdata_set.all()
    
    #Django provides a way to access the related ProductData objects 
    # from a UserData instance using the reverse relationship. 
    # By default, Django appends _set to the lowercase name of the 
    # related model to create this reverse relationship. So, 
    # for ProductData, it becomes productdata_set.
    
    return render(request, "sellerProfile.html", {"id": id,
                                                  "usersigned": usersigned,
                                                  "details": details})

# seller product edit delete
def edit(request, id):
    data = ProductData.objects.get(id = id)
    id = data.user_id
    if request.method == 'POST':
        print(request.POST)
        form = ProductDataForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse("shop:sellerProfile", args=[id]))
    return render(request, "sellerPage.html", {"data": data})

def delete(request, id):
    data = ProductData.objects.get(id = id)
    user_id = data.user_id
    data.delete()
    return redirect(reverse("shop:sellerProfile", args=[user_id]))
