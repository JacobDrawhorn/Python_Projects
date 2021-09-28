from django.contrib import admin
# add classes app to site admin
from .models import djangoClasses

admin.site.register(djangoClasses)