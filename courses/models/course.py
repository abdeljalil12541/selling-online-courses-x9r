from email.policy import default
from django.db import models


class Course(models.Model):
    name          = models.CharField(max_length=50)
    slug          = models.CharField(max_length=50, null=True, unique=True)
    description   = models.TextField(null=True)
    price         = models.IntegerField(default=0)
    discount      = models.IntegerField(default=0)
    active        = models.BooleanField(default=False)
    date          = models.DateTimeField(auto_now_add=True)
    thumbnail     = models.ImageField(upload_to='files/thumbnail')
    resource      = models.FileField(upload_to='files/resource')
    course_length = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
    
class CourseProperty(models.Model):
    description   = models.CharField(max_length=150, null=False)
    course        = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
    
    
class Tag(CourseProperty):
    # description   = models.CharField(max_length=150, null=False)
    # course        = models.ForeignKey(Course, on_delete=models.CASCADE)
    pass
    
    
class Prerequisite(CourseProperty):
    # prerequisite  = models.CharField(max_length=150, null=False)
    # course        = models.ForeignKey(Course, on_delete=models.CASCADE)
    pass
    
    
class Learning(CourseProperty):
    # Learning      = models.CharField(max_length=150, null=False)
    # course        = models.ForeignKey(Course, on_delete=models.CASCADE)
    pass