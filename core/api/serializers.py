from rest_framework import serializers

from core.models import Project,Building,Test,BuildingItem,People,Organization

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


