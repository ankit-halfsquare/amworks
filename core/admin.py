from django.contrib import admin

from .models import Building,Project,People,Organization,BuildingItem,TestBuilding,TestBuildingItem




class TestBuildingAdmin(admin.ModelAdmin):
    exclude=("guid ",)
    readonly_fields=('guid', )

class TestBuildingItemAdmin(admin.ModelAdmin):
    exclude=("guid ",)
    readonly_fields=('guid', )


# admin.site.register(TestBuilding, TestBuildingAdmin)
# admin.site.register(TestBuildingItem, TestBuildingItemAdmin)

admin.site.register(Project)
admin.site.register(People)
admin.site.register(Organization)
# admin.site.register(Building)
# admin.site.register(BuildingItem)

admin.site.register(TestBuilding)
admin.site.register(TestBuildingItem)