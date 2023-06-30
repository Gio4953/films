from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=255)
    year_of_release = models.IntegerField()
    length = models.DurationField()

    def __str__(self):
        return self.name
