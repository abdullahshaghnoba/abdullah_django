from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Game(models.Model):
    name= models.CharField(max_length=60, null=False, blank=True)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    genre=models.TextField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('Game_list')