from django.db import models

# Create your models here.

class rcf_user(models.Model):
    uid = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 16)
    email =models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    def __str__(self):
        return self.name
    