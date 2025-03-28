from django.db import models

# Create your models here.
from django.db import models

class StudentMarks(models.Model):
    student_id = models.IntegerField(unique=True)
    marks = models.IntegerField()