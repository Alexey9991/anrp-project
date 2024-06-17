from django.db import models


# Create your models here.
class DataForANRP(models.Model):
    date = models.DateField()
    hour_start = models.IntegerField()
    hour_end = models.IntegerField()
    num_cum = models.IntegerField()

    def __str__(self):
        return f'{self.date} {self.num_cum}'