from rest_framework import serializers

from core.models import Project,Building

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