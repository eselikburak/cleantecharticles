from django.contrib import admin
from .models import Home, Contact
# Register your models here.

admin.site.register(Home)
admin.site.register(Contact)

admin.site.site_header = "Cleantecharticles Administration"