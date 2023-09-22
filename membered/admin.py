from django.contrib import admin
from .models import Details
from .models import API
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .models import David

class DetailsAdmin(admin.ModelAdmin):
    list_display = ['Surname', 'Name', 'Address', 'Date_of_birth', 'Age', 'Telephone', 'WhatsApp', 'Email', 'Nationality', 'Sate_of_Origin', 'Session', 'Past_Qualification', 'Computer_Course']
    
class APIAdmin(admin.ModelAdmin):
    list_display = ['Pk', 'Name', 'Department']
    
class DavidAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Age', 'Date_Of_Birth']

admin.site.register(API, APIAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(David, DavidAdmin)
# Register your models here.
