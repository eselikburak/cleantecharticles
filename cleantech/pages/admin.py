from django.contrib import admin
from .models import Home
# Register your models here.

admin.site.register(Home)

admin.site.site_header = "Cleantecharticles Administration"