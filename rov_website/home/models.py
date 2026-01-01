# home/models.py
from django.db import models

class ProjectInfo(models.Model):
    title = models.CharField(max_length=200, default="ROV-KKHP")
    tagline = models.CharField(max_length=200, default="AI-Based Underwater ROV")
    description = models.TextField()
    team_size = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Project Info"
    
    def __str__(self):
        return self.title





