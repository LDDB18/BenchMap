from django.db import models


class Bench(models.Model):
    long = models.DecimalField(max_digits=13, decimal_places=10)
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    average_rating = models.DecimalField(max_digits=4, decimal_places=3)
    nb_voters = models.IntegerField(default=0)
    date_added = models.DateTimeField('date published')

    def __str__(self):
        return ("long:{} lat:{} average:{} nb_voters:{}".
                format(self.long, self.lat,self.average_rating, self.nb_voters))
