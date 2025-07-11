from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name


class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instances')
    year = models.IntegerField()
    semester = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    instructor = models.CharField(max_length=100)

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def __str__(self):
        return f"{self.course.name} - {self.year} {self.semester}"
