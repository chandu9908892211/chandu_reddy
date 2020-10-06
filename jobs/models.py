from django.db import models

# Create your models here.
class chandu(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    image=models.ImageField(upload_to='image/')
    