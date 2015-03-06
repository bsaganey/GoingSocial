from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    email = models.EmailField(max_length = 75)
    password = models.CharField(max_length = 75)
    name = models.CharField(max_length = 200)
    Hometown = models.CharField(max_length = 75)
    City = models.CharField(max_length = 75)
    birth = models.DateField()
    zipcode_validatior = RegexValidator(regex = '^\d{5}(?:[-\s]\d{4})?$')
    zipcode = models.CharField(validators = [zipcode_validatior], max_length = 5)