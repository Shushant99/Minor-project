from django.db import models

class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_photos/')  # main photo
    def __str__(self):
        return f'{self.roll_no} - {self.name}'

class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='student_photos/extra/')
    encoding_file = models.FilePathField(path='media/encodings', blank=True, null=True)

    def __str__(self):
        return f'Image of {self.student.name}'
