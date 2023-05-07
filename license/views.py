from django.shortcuts import render, redirect
from license.models import Bluebook_Fine, License_Fine, Nationalid, license,bluebook
from .forms import FineForm,FineForm1,LicenseForm,BluebookForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="login")
def createLicense(request):
    form=LicenseForm()
    if request.method == 'POST':
        form=LicenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("nationalid")

    context1={'form':form}
    return render(request,'createLicense.html',context1)

@login_required(login_url="login")
def updateLicense(request, pk):
    comp=license.objects.get(id=pk)
    form=LicenseForm(instance=comp)
    if request.method == 'POST':
        form=LicenseForm(request.POST,instance=comp)
        if form.is_valid():
            form.save()
            return redirect("license123")


    context1={'form':form}
    return render(request,'createLicense.html',context1)




@login_required(login_url="login")
def createBluebook(request):
    form=BluebookForm
    if request.method == 'POST':
        form=BluebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("nationalid")

    context1={'form':form}
    return render(request,'createBluebook.html',context1)

@login_required(login_url="login")
def updateBluebook(request, pk):
    comp=bluebook.objects.get(id=pk)
    form=BluebookForm(instance=comp)
    if request.method == 'POST':
        form=BluebookForm(request.POST,instance=comp)
        if form.is_valid():
            form.save()
            return redirect("bluebook123")


    context1={'form':form}
    return render(request,'createBluebook.html',context1)



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
                messages.info(request,'Invalid Credentials!!')
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
            newpost = form.save(commit=False)
            l = license.objects.get(id=newpost.lid.id)
            l.fine = newpost.amount
            l.save()
            form.save()
            return redirect('nationalid')
        else:
            print("Invalid")
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
    
    return render(request, 'license.html')

@login_required(login_url="login")
def bluebook123(request):   
    
    return render(request, 'bluebook.html')

@login_required(login_url="login")
def nationalid(request):


        return render(request,'nationalid.html')     
        # nationalid1= Nationalid.objects.filter(Nationalid__name__icontians=search,license__name__icontains=search,bluebook__name__icontains=search)


    

        
    


def s1(request):    

    if 'search' in request.GET:
            search=request.GET['search']
            n1 = Nationalid.objects.filter(id_number__icontains=search)
            return render(request,'s1.html',{'n1':n1})     
            # nationalid1= Nationalid.objects.filter(Nationalid__name__icontians=search,license__name__icontains=search,bluebook__name__icontains=search)


    else:
            messages.info(request,'Not found ')        
        

            return render(request,'s1.html')


def l1(request):    

    if 'search' in request.GET:
            search1=request.GET['search']
            license1= license.objects.get(license_number__icontains=search1)
            # penalty1= License_Fine.objects.get(national_id=license1)
            # return render(request, 'l1.html',{'license':license1,'pen':penalty1})
            return render(request, 'l1.html',{'license':license1})

            
    else:
        messages.info(request,'Not found ') 
        return render(request,'l1.html')       

def b1(request):
    if 'search' in request.GET:
            search1=request.GET['search']
            bluebook1= bluebook.objects.filter(book_number__icontains=search1)
            return render(request, 'b1.html',{'bluebook':bluebook1})


    else:
            messages.info(request,'Not found ') 
            return render(request,'b1.html')       


    




