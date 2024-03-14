from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
from .user_course import UserCourse

class Payment(models.Model):
    order_id      = models.CharField(max_length=150, null=True)
    payment_id    = models.CharField(max_length=150, null=True)
    user_course   = models.ForeignKey(UserCourse, null=True, blank=True, on_delete=models.CASCADE)
    user          = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    course        = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    date          = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=False)
    
    