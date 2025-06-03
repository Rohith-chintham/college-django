from django.shortcuts import render
from .models import ContactMessage

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save contact form submission
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'main/contact.html', {'success': True})
    
    return render(request, 'main/contact.html')
