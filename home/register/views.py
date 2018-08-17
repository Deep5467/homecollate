from django.shortcuts import render, HttpResponse
from .forms import Userform, pgform
from .models import register_user
from django.http import HttpResponseRedirect

def index(request):
    return render(request,'register/base.html',{})

def post_new(request):
    if request.method == "POST":
        x = Userform(request.POST)
        if x.is_valid():
            data = x.save(commit=False)
            data.save()
            return HttpResponse("succesfull data")

    else:
        form = Userform()
        return render(request, 'register/index.html',{'form': form})

def new_pg(request):
        if request.method == "POST":
            p = pgform(request.POST)
            if p.is_valid():
                data = p.save(commit=False)
                data.save()
                return HttpResponse("succesfull data")

        else:
            form = pgform()
            return render(request, 'register/index.html', {'form': form})