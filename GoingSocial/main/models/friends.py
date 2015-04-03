'''
from django.db import models
from main.models import MyUser


class Friend(models.Model):
    user = models.ForeignKey(MyUser)
    other = models.ForeignKey(MyUser)
'''