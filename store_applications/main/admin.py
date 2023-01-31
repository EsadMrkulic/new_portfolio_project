from django.contrib import admin
from .models import Position, Applicant, Manager, Application, Test

# Register your models here.
admin.site.register(Position)
admin.site.register(Applicant)
admin.site.register(Manager)
admin.site.register(Application)
admin.site.register(Test)