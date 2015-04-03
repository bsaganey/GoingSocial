from django.db import models
from main.models import MyUser
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]

class Post(models.Model):
    user = models.ForeignKey(MyUser)
    title = models.CharField(max_length = 32)
    body = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)