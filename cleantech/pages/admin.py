from django.contrib import admin
from .models import Home, Contact
# Register your models here.

admin.site.register(Home)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    

admin.site.site_header = "Cleantecharticles Administration"