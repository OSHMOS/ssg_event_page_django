from django.db import models


# Create your models here.
class Event(models.Model):
    dept = models.CharField(max_length=20, verbose_name='학과')
    num = models.CharField(max_length=10, verbose_name='학번')
    name = models.CharField(max_length=50, verbose_name='이름')
    photo = models.ImageField(upload_to='img/', verbose_name='인증 사진')

    def __str__(self):
        return f'{self.dept}, {self.num}, {self.name}'
