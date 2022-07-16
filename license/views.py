from django.shortcuts import render, redirect
from license.models import Bluebook_Fine, License_Fine, Nationalid, license,bluebook
from .forms import FineForm,FineForm1



# Create your views here.
def main(request):
    return render(request,'main.html')

def Fine(request):
    return render(request,'Fine.html')


def create1(request):
    form=FineForm()
    if request.method == 'POST':
        form=FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show1")

    context1={'form':form}
    return render(request,'licensefine.html',context1)


def create2(request):
    form=FineForm1()
    if request.method == 'POST':
        form=FineForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show2")

    context2={'form':form}
    return render(request,'bluebookfine.html',context2)

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

def show1(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        fines= License_Fine.objects.filter(Fine_Id__icontains=search1)
    else:
        fines = License_Fine.objects.all()
    
    
    return render(request,'show1.html',{'fines':fines} )

def show2(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        fines= Bluebook_Fine.objects.filter(Fine_Id__icontains=search1)
    else:
        fines = Bluebook_Fine.objects.all()


    
    return render(request,'show2.html',{'fines':fines} )

def removea(request, pk):
    Fines = License_Fine.objects.get(id=pk)

    if request.method == 'POST':
        Fines.delete()
        return redirect('/show1')

    context = {
        'fines': Fines,
    }

    return render(request, 'delete1.html', context)

def removeb(request, pk):
    Fines = Bluebook_Fine.objects.get(id=pk)

    if request.method == 'POST':
        Fines.delete()
        return redirect('/show2')

    context = {
        'fines': Fines,
    }

    return render(request, 'delete2.html', context)



  

    


def license123(request):
    if 'search' in request.GET:
        search1=request.GET['search']
        license1= license.objects.filter(name__icontains=search1)
    else:
        license1=license.objects.all()
    return render(request, 'license.html',{'license':license1})

def bluebook123(request):
    if 'search1' in request.GET:
        search12=request.GET['search1']
        bluebook1= bluebook.objects.filter(name__icontains=search12)
    else:
        bluebook1=bluebook.objects.all()

    
    return render(request, 'bluebook.html',{'bluebook':bluebook1})

def nationalid(request):


    if 'search' in request.GET:
        search=request.GET['search']
        n1 = Nationalid.objects.filter(id_number__icontains=search)
         
        # nationalid1= Nationalid.objects.filter(Nationalid__name__icontians=search,license__name__icontains=search,bluebook__name__icontains=search)


    else:
        n1= Nationalid.objects.all()


        
    

    return render(request,'nationalid.html',{'n1':n1})


