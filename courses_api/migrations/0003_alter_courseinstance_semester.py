# Generated by Django 5.0.14 on 2025-07-01 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_api', '0002_course_prerequisites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinstance',
            name='semester',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
