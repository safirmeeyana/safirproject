import datetime

from django.db import models

# Create your models here.
class place(models.Model):
    Name=models.CharField(max_length=150)
    Image=models.ImageField(upload_to='picture')
    Description=models.TextField()
    Price=models.IntegerField()
    Offer=models.BooleanField(default=False)




class blog(models.Model):
    date=models.DateField(default=datetime.date.today)
    Name = models.CharField(max_length=150)
    Image = models.ImageField(upload_to='picture')
    Description = models.TextField()
    Content = models.TextField()
