from django.db import models
from django.contrib.auth.models import User
class Personne(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=100)
    ville=models.CharField(max_length=40)
    date_create=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="personnes"
    def __str__(self):
        return self.nom
    def get_complete_str(self):
        return f"{self.adresse} {self.ville}"
    
