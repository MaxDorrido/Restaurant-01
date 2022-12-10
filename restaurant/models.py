from django.db import models

# Create your models here.

class nationality(models.Model):
    nationality = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.nationality

class restaurant(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc =models.TextField(max_length=150)
    price =models.IntegerField()
    nationality =models.ForeignKey(nationality, default=None, on_delete=models.CASCADE)

