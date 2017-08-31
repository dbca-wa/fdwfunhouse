from django.contrib import admin
from .models import ForeignAuthUser, UserComment

# Register your models here.
admin.site.register([ForeignAuthUser, UserComment])