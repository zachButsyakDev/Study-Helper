from django.db import models
from users.models import User


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=255)
    
    def __str__(self):
        return self.courseName