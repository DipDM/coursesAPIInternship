from django.urls import path
from . import views

urlpatterns = [
    path('courses', views.CourseListCreateView.as_view()),
    path('courses/<int:pk>', views.CourseDetailUpdateDeleteView.as_view(), name='course-detail-update-delete'),


    path('instances', views.CourseInstanceCreateView.as_view()),
    path('instances/<int:pk>', views.CourseInstanceUpdateView.as_view()),
    path('instances/<int:pk>', views.CourseInstanceRetrieveByIdView.as_view()),
    path('instances/<int:year>/<str:semester>', views.CourseInstanceListView.as_view()),
    path('instances/<int:year>/<str:semester>/<int:course_id>', views.CourseInstanceDetailView.as_view(),name='instance-detail-delete'),
]
