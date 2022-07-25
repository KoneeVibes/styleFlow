from django.db import models

class logindetails(models.Model):
    username: models.CharField(max_length=200)
    password: models.CharField(max_length=10)

    def __str__(self):
        return self.username