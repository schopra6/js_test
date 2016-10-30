from django.db import models

class album(models.Model):
    genre=models.CharField(max_length=50)
    playlist = models.CharField(max_length=50)
    number=models.IntegerField(max_length=10)
    def __str__(self):
        return self.genre

# Create your models here.
class song(models.Model):
    albu=models.ForeignKey(album,on_delete=models.CASCADE)

