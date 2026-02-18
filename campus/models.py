from django.db import models

# Create your models here.
class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class StudentIDCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=20)

    def __str__(self):
        return f"ID Card for {self.student}"
    

class CourseDescription(models.Model):
    course = models.OneToOneField('Course', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Description for {self.course}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f"{self.code} - {self.name}"