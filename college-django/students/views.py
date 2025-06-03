from django.shortcuts import render, get_object_or_404
from .models import Student, Result

# For demonstration, let's assume a single student with id=1.
# In a real app, you'd get the logged-in user or use dynamic IDs.

def dashboard(request):
    student = get_object_or_404(Student, id=1)  # Replace with dynamic logic
    context = {
        'student': student,
        'results_count': student.results.count(),
    }
    return render(request, 'students/dashboard.html', context)

def result_list(request):
    student = get_object_or_404(Student, id=1)  # Replace with dynamic logic
    results = student.results.all()
    return render(request, 'students/result_list.html', {'results': results})

def profile(request):
    student = get_object_or_404(Student, id=1)  # Replace with dynamic logic
    return render(request, 'students/profile.html', {'student': student})
