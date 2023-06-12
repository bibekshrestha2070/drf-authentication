from django.contrib import admin
from apps.authentication_app.models import CustomUser

# Register your models here.

admin.site.register(CustomUser)
