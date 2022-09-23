
from django.shortcuts import render, redirect
from .models import Review, About, Contact
from projects_experiences.models import Project
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
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        if len(message) < 10:
            messages.warning(request, "Feedback length should be greator than 10 characters")
            return redirect('contact')
        
        feed = Contact.objects.create(
            first_name=fname,
            last_name=lname,
            email = email,
            message = message
        )
        feed.save()

        print(f"\n\n {fname} {lname} \n\n {email} \n\n {message} \n\n")
        messages.success(request,"Message sent successfully")
        return redirect('/')
    
    return render(request, 'contact.html')

def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }
    return render(request, 'about.html', context)

def leave_review(request):
    if request.method == 'POST' and request.FILES:
        name = request.POST['name']
        position = request.POST['position']
        review = request.POST['review']
        image = request.FILES['image']

        if len(review) < 15:
            messages.warning(request, "Feedback length should be greator than 15 characters")
            return redirect('leave_review')

        review = Review.objects.create(
            name=name,
            position=position,
            message = review,
            image=image
        )

        messages.success(request,"Review sent successfully,  Thank you for the Review")
        return redirect('/')
        
    return render(request, 'leave_review.html')


# Create your views here.
def portfolio(request):
    portfolios = Project.objects.all()
    context = {
        'portfolios': portfolios,
    }
    return render(request, 'portfolio.html', context)