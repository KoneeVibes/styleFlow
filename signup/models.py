from django.db import models

class user(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.username
        
