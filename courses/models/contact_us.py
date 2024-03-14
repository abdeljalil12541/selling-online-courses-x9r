from django.db import models
from django.contrib.auth.models import User


class ContactUs(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name  = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contact Us'
        
    def __str__(self):
        return self.name