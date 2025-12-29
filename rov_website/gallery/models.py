from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    # 🔹 REQUIRED for your existing functionality
    category = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Existing ordering logic
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
