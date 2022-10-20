# Generated by Django 4.1.1 on 2022-10-06 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education_app', '0002_assessment_work_students_work_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_assessments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_assessments', to=settings.AUTH_USER_MODEL),
        ),
    ]
