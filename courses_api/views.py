from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# CourseInstance Views
class CourseInstanceCreateView(generics.ListCreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CourseInstanceListView(APIView):
    def get(self, request, year, semester):
        instances = CourseInstance.objects.filter(year=year, semester=semester)
        serializer = CourseInstanceSerializer(instances, many=True)
        return Response(serializer.data)

class CourseInstanceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer


class CourseInstanceDetailView(APIView):
    def get(self, request, year, semester, pk):
        try:
            instance = CourseInstance.objects.get(pk=pk, year=year, semester=semester)
            serializer = CourseInstanceSerializer(instance)
            return Response(serializer.data)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, year, semester, pk):
        try:
            instance = CourseInstance.objects.get(pk=pk, year=year, semester=semester)
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CourseInstance.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CourseInstanceRetrieveByIdView(generics.RetrieveAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
    lookup_field = 'pk'
 