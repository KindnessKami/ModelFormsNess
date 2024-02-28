from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)
    DOB = models.DateField()
    age = models.IntegerField()

    class Meta:
        db_table = 'students'


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_Name = models.CharField(max_length=20)
    emailaddress = models.EmailField()

    def __str__(self):
        return self.first_name


class Parents(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)
    DOB = models.DateField()
    age = models.IntegerField()


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    duration = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    created_at = models.DateField
