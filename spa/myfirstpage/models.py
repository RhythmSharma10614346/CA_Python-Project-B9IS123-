from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    