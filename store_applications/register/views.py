from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm

# Create your views here.

def register(request):
    submitted = False
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return HttpResponseRedirect("/register?submitted=True")
    else:
        form = RegisterForm(request.POST)
        if "submitted" in request.GET:
            submitted = True
        return render(request, "register/register.html", {"form": form, "submitted": submitted})