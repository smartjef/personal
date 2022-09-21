from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio.html', context)