from django.contrib import admin
from .models import Candidate

# Register your models here.

class Candidateadmin(admin.ModelAdmin):
    readonly_fields = ("login_time", "logout_time","modified_date","created_date")


admin.site.register(Candidate,Candidateadmin)