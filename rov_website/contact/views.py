# contact/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            contact_msg.save()
            messages.success(request, 'Message sent successfully! We will get back to you soon.')
            return redirect('contact:success')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def contact_success(request):
    return render(request, 'contact/success.html')