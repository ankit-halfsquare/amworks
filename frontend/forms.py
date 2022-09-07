from django.forms import ModelForm
from core.models import TestBuilding,TestBuildingItem


class BuildingForm(ModelForm):
    class Meta:
        model = TestBuilding
        fields = '__all__'
        exclude=("create_date","update_date")



class BuildingForm2(ModelForm):
    class Meta:
        model = TestBuilding
        fields = ('organization_id', 'name','code','city','state','country','zip','status','create_user','obsolete')
       


class BuildingForm3(ModelForm):
    class Meta:
        model = TestBuilding
        fields = ('ta1_alias','ta2_alias','ta3_alias','ta4_alias','ta5_alias','ta6_alias','ta7_alias','ta8_alias','ta9_alias','ta10_alias','ta11_alias','ta12_alias','ta13_alias','ta14_alias','ta15_alias','ta16_alias','ta17_alias','ta18_alias','ta19_alias','ta20_alias')
        