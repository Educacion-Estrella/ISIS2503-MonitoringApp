from django.db import models

class Psicologo (models.Model):
    nombre= models.CharField(max_lenght=50)
    edad= models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.nombre,self.edad)