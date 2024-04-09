from django.db import models

# Create your models here.
class Advocate(models.Model):
    username = models.CharField(max_length=50)
    bio = models.TextField()
    
    def __str__(self):
        return self.username
    
    