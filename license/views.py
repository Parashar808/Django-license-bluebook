from django.shortcuts import render, redirect
from license.models import Bluebook_Fine, License_Fine, Nationalid, license,bluebook
from .forms import FineForm,FineForm1
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
# def register(request):


#     if request.method== 'POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         username=request.POST['username']
#         password1=request.POST['password1']
#         password2=request.POST['password2']

#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'user name taken')
#                 return redirect('/')            
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email taken')
#                 return redirect('/')
#             else:
#                 user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
#                 user.save()
#                 print('user created')
#                 return redirect('/')
#         else:
#             messages.info(request,'password not matching')
#             return redirect('/')


        
#     return render(request,'register.html')

def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect("nationalid") 

            else:
                messages.info(request,'Invalid ')
                return redirect('login')

        else:
            return render(request,'login.html')
         


@login_required(login_url="login")    
def logout(request):
    auth.logout(request)
    return redirect('/')







def main(request):
    return render(request,'main.html')

@login_required(login_url="login")
def Fine(request):
    return render(request,'Fine.html')

@login_required(login_url="login")
def create1(request):
    form=FineForm()
    if request.method == 'POST':
        form=FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show1")

    context1={'form':form}
    return render(request,'licensefine.html',context1)

@login_required(login_url="login")
def create2(request):
    form=FineForm1()
    if request.method == 'POST':
        form=FineForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show2")

    context2={'form':form}
    return render(request,'bluebookfine.html',context2)

@login_required(login_url="login")
def update1(request, pk):
    comp=License_Fine.objects.get(id=pk)
    form=FineForm(instance=comp)
    if request.method == 'POST':
        form=FineForm(request.POST,instance=comp)
        if form.is_valid():
            form.save()
            return redirect("/show1")


    context1={'form':form}
    return render(request,'licensefine.html',context1)

@login_required(login_url="login")
def update2(request, pk):
    comp=Bluebook_Fine.objects.get(id=pk)
    form=FineForm1(instance=comp)
    if request.method == 'POST':
        form=FineForm1(request.POST,instance=comp)
        if form.is_valid():
            form.save()
            return redirect("/show2")


    context1={'form':form}
    return render(request,'bluebookfine.html',context1)


@login_required(login_url="login")
def show1(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        fines= License_Fine.objects.filter(Fine_Id__icontains=search1)
    else:
        fines = License_Fine.objects.all()
    
    
    return render(request,'show1.html',{'fines':fines} )

@login_required(login_url="login")
def show2(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        fines= Bluebook_Fine.objects.filter(Fine_Id__icontains=search1)
    else:
        fines = Bluebook_Fine.objects.all()


    
    return render(request,'show2.html',{'fines':fines} )

@login_required(login_url="login")
def removea(request, pk):
    Fines = License_Fine.objects.get(id=pk)

    if request.method == 'POST':
        Fines.delete()
        return redirect('/show1')

    context = {
        'fines': Fines,
    }

    return render(request, 'delete1.html', context)

@login_required(login_url="login")
def removeb(request, pk):
    Fines = Bluebook_Fine.objects.get(id=pk)

    if request.method == 'POST':
        Fines.delete()
        return redirect('/show2')

    context = {
        'fines': Fines,
    }

    return render(request, 'delete2.html', context)



  

    


@login_required(login_url="login")
def license123(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        license1= license.objects.filter(name__icontains=search1)
    else:
        license1=license.objects.all()
    return render(request, 'license.html',{'license':license1})

@login_required(login_url="login")
def bluebook123(request):
    if 'search1' in request.GET:
        search12=request.GET['search1']
        bluebook1= bluebook.objects.filter(name__icontains=search12)
    else:
        bluebook1=bluebook.objects.all()

    
    return render(request, 'bluebook.html',{'bluebook':bluebook1})

@login_required(login_url="login")
def nationalid(request):


    if 'search' in request.GET:
        search=request.GET['search']
        n1 = Nationalid.objects.filter(id_number__icontains=search)
         
        # nationalid1= Nationalid.objects.filter(Nationalid__name__icontians=search,license__name__icontains=search,bluebook__name__icontains=search)


    else:
        n1= Nationalid.objects.all()


        
    

    return render(request,'nationalid.html',{'n1':n1})


