from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    ra = models.CharField(max_length=15)
    dec = models.CharField(max_length=15)
