from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstance
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('course', None)  # Prevent changing course
        return super().update(instance, validated_data)
