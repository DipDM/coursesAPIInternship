from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.CourseListCreateView.as_view()),
    path('courses/<int:pk>', views.CourseDetailView.as_view()),
    path('courses/<int:pk>/update', views.CourseUpdateView.as_view()),


    path('instances', views.CourseInstanceCreateView.as_view()),
    path('instances/<int:pk>/update', views.CourseInstanceUpdateView.as_view()),
    path('instances/<int:pk>', views.CourseInstanceRetrieveByIdView.as_view()),
    path('instances/<int:year>/<str:semester>', views.CourseInstanceListView.as_view()),
    path('instances/<int:year>/<str:semester>/<int:pk>', views.CourseInstanceDetailView.as_view()),
]
