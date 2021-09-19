from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import PepoleForm
from django.http import HttpResponse
from .models import People
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from faker import Faker
from django.core.paginator import Paginator
from django.views.generic import ListView



def baseview(request):
    template_name='Page_App/base.html'
    context={}
    return render(request,template_name,context)

@login_required(login_url='login')
def submitview(request):
    form = PepoleForm()

    if request.method=='POST':
        form = PepoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showlist')

    template_name='Page_App/submitform.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def showALLview(request):
    all_people = People.objects.all()
    context = {'all_people': all_people}
    template_name = 'Page_App/showlist.html'
    return render(request, template_name, context)


@login_required(login_url='login')
def deletepersonview(request,id):
    person = People.objects.get(id=id)
    person.delete()
    return redirect('showlist')

@login_required(login_url='login')
def updatepersonview(request,id):
    obj = People.objects.get(id=id)
    form= PepoleForm(instance=obj)

    if request.method=='POST':
        form = PepoleForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showlist')

    template_name='Page_App/submitform.html'
    context = {'form': form}
    return render(request, template_name, context)


def addFakePeople(request):
    fake = Faker()
    for x in range(10):
        nm = fake.name()
        con = fake.country()
        add = fake.address()
        p = People(name=nm, address=add, country=con)
        p.save()
        print(p.name, p.country, p.address)
    return redirect('showlist')


#function based paginator
@login_required(login_url='login')
def pageview(request):
    all_people = People.objects.all()
    paginator = Paginator(all_people, 5) # Shows 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Page_App/list.html', {'page_obj': page_obj})



#class based pagination
class PageListView(ListView):
    model = People
    paginate_by = 2
    template_name = 'Page_App/class-based-list.html'
    context_object_name = "people"  #obj_list(default context)



