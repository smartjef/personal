from datetime import datetime
from django.shortcuts import render

from resume.models import Education
from skills.models import ProgrammingLanguage, Framework, Tool
# Create your views here.
def resume(request):
    education = Education.objects.all()
    p_languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    tools = Tool.objects.all()
    context = {
        'education' : education,
        'p_languages' : p_languages,
        'frameworks' : frameworks,
        'tools' : tools,
    }
    return render(request, 'resume.html', context)

