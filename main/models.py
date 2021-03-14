from django.db import models

import datetime

# Create your models here.
class post(models.Model):
    event_name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    # location = models.PointField()
    date = models.DateTimeField(default = datetime.datetime.now)
    image = models.ImageField()
    is_liked = models.BooleanField(default=False)

