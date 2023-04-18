from django.db import models

# Create your models here.


class Event(models.Model):
    dept = models.CharField(max_length=20)
    num = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/')

    def __str__(self):
        return f'{self.dept}, {self.num}, {self.name}'
