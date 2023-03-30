
from django.core.mail import message
from django.shortcuts import render

# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from login.models import Departments, Courses, Complete


# Create your views here.





# # Create your views here.




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        # user=User.objects.create_user(username=username,password=password)
        # user.save();
        # print('user created')
    #     return HttpResponseRedirect('login')
    #
    #


        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME ALREADY EXIST')
                return HttpResponseRedirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'MAIL ID TAKEN')
                return HttpResponseRedirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return HttpResponseRedirect ('login')
        else:
            messages.info(request, 'password not matched')
            return HttpResponseRedirect('register')

    #
    return render(request, 'register.html')



def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        # return HttpResponseRedirect('details')

        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('welcome')
        else:
            messages.info(request,'invalid credentials')
            return redirect('register')

    return render(request, "login.html")

def welcome(request):

         return render(request, 'welcome.html')

def details(request):

    return render(request,'details.html')

def order(request):
    # if request.method=='POST':
    #     username=request.POST['username']
    #     mailid=request.POST['email']
    #     user=auth.authenticate(username=username,mailid=mailid)
    #     return HttpResponseRedirect('order')


    return render (request,"order.html")





# def load_branches (request):
#     department_id = request .GET.get('course')
#     branches = Branch.objects.filter.(department_id=department_id).order_by('name'))
#     return render(request,'details.html')






# def depDetail(request,):
#     try:
#         product=Product.objects.get(category__slug=c_slug,slug=product_slug)
#     except Exception as e:
#         raise e
#
#     return render(request,'product.html',{'product':product})



# def view_items(request):
#     name = Name.objects.all()
#
#     context = {
#         'places': place,
#         'pictures': picture
#     }
#     return render(request, 'index.html', context)


