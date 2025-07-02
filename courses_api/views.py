from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.prefetch_related('prerequisites').all()
    serializer_class = CourseSerializer

class CourseDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.prefetch_related('prerequisites').all()
    serializer_class = CourseSerializer

    def delete(self, request, *args, **kwargs):
        course = self.get_object()

        # Check if this course is a prerequisite to any other
        if course.prerequisites.exists():
            return Response(
                {"error": "Cannot delete: Course is a prerequisite for other courses."},
                status=status.HTTP_409_CONFLICT
            )

        # Check if course has instances
        if course.instances.exists():
            return Response(
                {"error": "Cannot delete: Course has existing delivery instances."},
                status=status.HTTP_409_CONFLICT
            )

        return super().delete(request, *args, **kwargs)


# CourseInstance Views
class CourseInstanceCreateView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.select_related('course').all()
    serializer_class = CourseInstanceSerializer



class CourseInstanceListView(APIView):
    def get(self, request, year, semester):
        instances = CourseInstance.objects.select_related('course').filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(instances, many=True)
        return Response(serializer.data)

class CourseInstanceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer


class CourseInstanceDetailView(APIView):
    def get(self, request, year, semester, course_id):
        try:
            instance = CourseInstance.objects.select_related('course').get(course_id=course_id, year=year, semester=semester)
            serializer = CourseInstanceSerializer(instance)
            return Response(serializer.data)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, year, semester, course_id):
        try:
            instance = CourseInstance.objects.get(course_id=course_id, year=year, semester=semester)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CourseInstanceRetrieveByIdView(generics.RetrieveAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
    lookup_field = 'pk'
 