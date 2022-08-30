from django.forms import ModelForm
from core.models import TestBuilding,TestBuildingItem


class BuildingForm(ModelForm):
    class Meta:
        model = TestBuilding
        fields = '__all__'
        exclude=("create_date","update_date")