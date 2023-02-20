from django.db import models
from django.db import models

# Create your models here.

class videoAns(models.Model):
    ansId = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255,null=True)
    assessment_name = models.CharField(max_length=300,null=True)
    videoAns = models.FileField(upload_to='media',blank=True)
    trasnscript = models.CharField(max_length=10000,null=True)
    

    def __str__(self):
        return self.user_name

