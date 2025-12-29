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


# about/models.py
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


# gallery/models.py
class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(
        max_length=50,
        choices=[
            ('vehicle', 'Vehicle'),
            ('testing', 'Testing'),
            ('team', 'Team'),
            ('event', 'Event'),
        ]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title


# team/models.py
class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('leader', 'Team Leader'),
        ('mechanical', 'Mechanical Engineer'),
        ('electrical', 'Electrical Engineer'),
        ('software', 'Software Developer'),
        ('business', 'Business Manager'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"


# contact/models.py
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"