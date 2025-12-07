from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('TEACHER', 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='TEACHER')

    def is_admin(self):
        return self.role == 'ADMIN'

    def is_teacher(self):
        return self.role == 'TEACHER'
