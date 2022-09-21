from datetime import datetime
import imp
from django.shortcuts import render

from resume.models import Education
from projects_experiences.models import Project, Experience, Referees
from skills.models import ProgrammingLanguage, Framework, Tool
# Create your views here.
def resume(request):

    education = Education.objects.all()
    p_languages = ProgrammingLanguage.objects.all()
    frameworks = Framework.objects.all()
    tools = Tool.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    referees = Referees.objects.all()
    context = {
        'education' : education,
        'p_languages' : p_languages,
        'frameworks' : frameworks,
        'tools' : tools,
        'projects' : projects,
        'experiences' : experiences,
        'referees' : referees,
    }
    return render(request, 'resume.html', context)

