from django.contrib import admin

from .models import Building, Project,Test

admin.site.register(Building)
admin.site.register(Project)
admin.site.register(Test)