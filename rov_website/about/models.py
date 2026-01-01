from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    features = models.TextField(help_text="Separate features with commas")
    image = models.ImageField(upload_to='vehicles/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.year})"
class Subdivision(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fa-cog")
    
    def __str__(self):
        return self.name