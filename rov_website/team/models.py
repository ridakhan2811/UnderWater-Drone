from django.db import models


class Subdivision(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


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
    subdivision = models.ForeignKey(
        Subdivision,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"
