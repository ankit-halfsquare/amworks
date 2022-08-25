from django.contrib import admin

from .models import Building,Project,People,Organization,BuildingItem


admin.site.register(Building)
admin.site.register(Project)
admin.site.register(People)
admin.site.register(Organization)
admin.site.register(BuildingItem)
# admin.site.register(Test)