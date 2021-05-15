from django.shortcuts import render, redirect#it sends to another page
from .models import Category, Product, User, Kassenzettel
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewList, CreateUserForm, CreateKassen# this imports from the forms.py file that you  just created thad takes the respective form from it
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#======= view for the logins =========

def login1(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            redirection = redirect('/')
            return redirection
        else:
            messages.info(request, 'Username failed')




    return render(request, 'store/registration/logintrue.html')

def logout1(request):
    logout(request)
    return redirect('/')



#====== creates a new users ======>
def create(request):
    form = CreateUserForm()
    if request.method == "POST":#post for changing something
        form = CreateUserForm(request.POST)

        if form.is_valid():

            # n = form.cleaned_data["name"]
            # Category.objects.get(id=1)
            # # if "Tilapia" not in n:
            # #     raise ValidationError(n)
            # # else:
            # #     raise ValidationError(Category.objects.get(id=1))
            #
            # t = Category(slug=n)
            # t.save()

        #retu
            #HttpResponseRedirect()
            ValidationError('exito')
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'cuenta creada para' + user)
            response = redirect('/login1/')
            return response

    context= {"form": form}
    return render(request, 'store/registration/login.html', context)


# ======= on this view we get the inormation from the database and change the settings so it can be seen every where
def categories(request):
    return {
        'categories': Category.objects.all()
        # this return function is equivalent to calling the sql of all dadta from Category and putting it on the object variable
    }

#========= on this section we handle the inforamtion of hte products and send it to the home.html file
def all_products(request):  # inside of request goes the users request information
    form = CreateKassen()
    # ===== creates the logic necessary to obtain the data from post and pass it to the shopping car
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        cuser = request.POST.get('currentuser')

        currentuser = User.objects.get(id=cuser)

        kassen = Kassenzettel()
        kassen.name = name
        kassen.price = price

        kassen.created_by = currentuser
        kassen.kassenzettel = currentuser

        kassen.save()

    products = Product.objects.all()  # this line of code is the SQL equivalent to call all objects from my model
    return render(request, 'store/home.html',
                  {'products': products})  # loads the associated information into the templates

#========= on this view we handel the topics of who is our team, who we are, video playing, contact us, and locaition =======
def index(request):  # inside of request goes the users request information
    products = Product.objects.all()# this line of code is the SQL equivalent to call all objects from my model

    # ===== creates the logic necessary to obtain the data from post and pass it to the shopping car
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        cuser = request.POST.get('currentuser')

        currentuser = User.objects.get(id=cuser)

        kassen = Kassenzettel()
        kassen.name = name
        kassen.price = price

        kassen.created_by = currentuser
        kassen.kassenzettel = currentuser

        kassen.save()

    # return render(request, 'store/home.html', {'products': products})#loads the associated information into the templates
    return render(request, 'store/index.html', {'products': products})

@login_required()
def check_out(request):
    i = 0
    kassen = Kassenzettel.objects.filter(kassenzettel = request.user)
    for k in kassen:
        i = i + k.price

    return render(request, 'store/check-out.html', {'kassenzettel1': kassen, 'total': i})
