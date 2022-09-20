from django.shortcuts import render
from .models import Review, About
from django.contrib import messages
# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request,'index.html', context)

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        print(first_name, last_name, email, message)
        messages.success(request, 'Message sent successfully.')
    return render(request, 'contact.html')

def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

def leave_review(request):
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
        msg = request.POST.get('message',"Some wonderfull review")

        print(name, position, msg)
        # Review.objects.create(
        #     name=name,
        #     position=position,
        #     message=message
        # )
        messages.success(request, 'Review sent successfully.')
        
    return render(request, 'leave_review.html')