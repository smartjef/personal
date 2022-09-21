from datetime import datetime
from django.shortcuts import render

from resume.models import Education
import datetime
# Create your views here.
def resume(request):
    education = Education.objects.all()
    context = {
        'education' : education,
    }
    return render(request, 'resume.html', context)

