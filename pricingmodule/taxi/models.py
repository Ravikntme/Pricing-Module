from django.db import models

# Create your models here.
class Rates(models.Model):
    dbp = models.FloatField()
    tbp = models.FloatField()