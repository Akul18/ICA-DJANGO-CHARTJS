from django.db import models

class PITAirportTrainFact(models.Model):
   dateAdded = models.DateField(auto_now_add=True)
   funFact = models.TextField(blank=True)
   ranking = models.TextField(blank=True)

   def __str__(self):
       return f"{self.dateAdded}: {self.funFact[40:]} with ranking {self.ranking}..."
