from django.db import models

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name
class Courses(models.Model):
    subject = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Complete(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


