from django.db import models

# Create your models here.
class Rates(models.Model):
    dbp = models.FloatField()
    tbp = models.FloatField()

class Timebase(models.Model):
    name =models.CharField(max_length=50, null=True, blank=True)
    variable_tbp = models.FloatField()