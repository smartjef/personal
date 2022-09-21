from django.shortcuts import render
from projects_experiences.models import Project
# Create your views here.
def portfolio(request):
    portfolios = Project.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio.html', context)