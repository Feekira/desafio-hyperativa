from django.db import models

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=50)
    lote = models.CharField(max_length=50)
    card_number = models.CharField(max_length=50)

    def __str__(self):
        return self.identifier