# gallery/views.py
from django.shortcuts import render
from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all()
    categories = GalleryImage.objects.values_list('category', flat=True).distinct()
    
    context = {
        'images': images,
        'categories': categories,
    }
    return render(request, 'gallery/gallery.html', context)

def gallery_by_category(request, category):
    images = GalleryImage.objects.filter(category=category)
    categories = GalleryImage.objects.values_list('category', flat=True).distinct()
    
    context = {
        'images': images,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery/gallery.html', context)
