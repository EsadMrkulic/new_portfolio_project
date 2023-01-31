from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Position, Applicant, Manager, Application
from .forms import ApplicationSubmission, ApplicantSignUp, Test

# Create your views here.


def home(request):
    return render(request, "main/home.html", {})


def all_positions(request):
    positions = Position.objects.all()
    return render(request, "main/positions.html", {"positions": positions})


'''def positions(response, job_title):
    pos = Position.objects.get(job_title=job_title)
    #return HttpResponse("<h1>%s</h1>" % pos.job_description)
    return render(response, "main/positions.html", {"pos": pos})'''



'''def application(response):
    return HttpResponse("<h1>Apply for a position using the application below!</h1>")'''


def submitapp(request):
    submitted = False
    if request.method == "POST":
        form = ApplicationSubmission(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect("/apply?submitted=True")

    else:
        form = ApplicationSubmission()
        if "submitted" in request.GET:
            submitted = True
        return render(request, "main/apply.html", {"form": form, "submitted": submitted})

def applicant(request):
    submitted = False
    if request.method == "POST":
        form = ApplicantSignUp(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            
        return HttpResponseRedirect("/applicant?submitted=True")

    else:
        form = ApplicantSignUp()
        if "submitted" in request.GET:
            submitted = True
        return render(request, "main/applicant.html", {"form": form, "submitted": submitted})

def test(request):
    submitted = False
    if request.method == "POST":
        form = Test(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/test?submitted=True")

    else:
        form = Test()
        if "submitted" in request.GET:
            submitted = True
        return render(request, "main/test.html", {"form": form, "submitted": submitted})