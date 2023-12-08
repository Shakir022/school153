from django.db import models
from django.contrib.auth.models import AbstractUser

class Grade(models.Model):
    name=models.CharField('класс', max_length=20)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    birthday = models.DateField('день рождения', null=True, blank=True)
    gender = models.CharField('пол',
        max_length=7,
        choices=[('мужчина', 'мужчина'),('женщина', 'женщина')],
        null=True, blank=True
    )
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, null=True, blank=True,)

