from django.db import models


class Regione(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Provincia(models.Model):
    nome = models.CharField(max_length=100)
    regione = models.ForeignKey(Regione, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
