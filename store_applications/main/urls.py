from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    #path("<application>", views.application, name="application"),
    path("positions/", views.all_positions, name="all_positions"),
    path("apply/", views.submitapp, name="apply"),
    path("applicant/", views.applicant, name="sign_up"),
    path("test/", views.test, name="test"),
]