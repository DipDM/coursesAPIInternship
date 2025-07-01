from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    prerequisites = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, required=False
    )

    class Meta:
        model = Course
        fields = '__all__'
    
    def validate_prerequisites(self, value):
        for course in value:
            if not Course.objects.filter(pk=course.pk).exists():
                raise serializers.ValidationError(f"Invalid prerequisite:Course with ID {course.pk} does not exist.")
        return value

class CourseInstanceSerializer(serializers.ModelSerializer):

    course= serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = CourseInstance
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('course', None)  # Prevent changing course
        return super().update(instance, validated_data)
