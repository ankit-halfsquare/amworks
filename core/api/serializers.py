from rest_framework import serializers

from core.models import Project,Building,BuildingItem,People,Organization,TestBuilding,TestBuildingItem

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('id','name', 'company_id')


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        # fields = '__all__'
        fields = ('id','name', 'code')



class BuildingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingItem
        # fields = '__all__'
        fields = ('id','name', 'code')


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        # fields = '__all__'
        fields = ('id','name_first', 'name_last')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        # fields = '__all__'
        fields = ('id','name', 'code')





class TestBuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBuilding
        fields = '__all__'
        # fields = ('id','name', 'code')



class TestBuildingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBuildingItem
        fields = '__all__'
        # fields = ('id','name', 'code')


