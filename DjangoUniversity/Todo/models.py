from django.db import models

# Create your models here.
# https://www.youtube.com/watch?v=-gKhnaTUXrM&t=333s
class Tarea(models.Model):
    tarea = models.CharField(max_length=100)
    prioridad = models.IntegerField()

    def __str__(self):
        return self.tarea