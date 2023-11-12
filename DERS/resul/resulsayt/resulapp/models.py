from django.db import models

# Create your models here.

class TELEBE(models.Model):
    qrup = models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    teqaud=models.BooleanField(default=True)
    sekil=models.ImageField(upload_to='photos/%Y/%m/%d/')


