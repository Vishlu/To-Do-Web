
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .forms import Studentregistration
from .models import User


# this function is used to add the data


def add_show(request):
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            fm = Studentregistration()
            return redirect('show/')
            
    else:
        fm = Studentregistration()
    reg = User.objects.all()
    # print(reg)
    return render(request, 'app/add.html',  {'form':fm, 'disp': reg})

# {'disp': reg},

# this function is used to show the data
def show_data(request):
    reg = User.objects.all()
    return render(request, 'app/show.html', {'disp': reg})



# this function is used to delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        # return redirect('show')

# this function is used to update the data
def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('show')
    else:
        pi = User.objects.get(pk=id)
        fm = Studentregistration(instance=pi)

    return render(request, 'app/update.html', {'form': fm})
