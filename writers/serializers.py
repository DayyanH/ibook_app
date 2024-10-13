from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user']
        read_only_fields = ['created_at', 'updated_at', 'user']