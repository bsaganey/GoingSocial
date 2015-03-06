from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

<<<<<<< HEAD:GoingSocial/main/models/myusers.py
class MyUser(models.Model):
    user = models.OneToOneField(User) 
=======
class User(models.Model):
    username = models.CharField(max_length = 75)
>>>>>>> 63f77db2734457c68d83ba5c72fc8fe4b14dbfa6:GoingSocial/main/models/users.py
    email = models.EmailField(max_length = 75)
    name = models.CharField(max_length = 200)
    hometown = models.CharField(max_length = 75)
    city = models.CharField(max_length = 75)
    birth = models.DateField()
    zipcode_validatior = RegexValidator(regex = '^\d{5}(?:[-\s]\d{4})?$')
    zipcode = models.CharField(validators = [zipcode_validatior], max_length = 5)