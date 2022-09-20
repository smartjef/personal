from django.shortcuts import render
from .models import Review
# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request,'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')