from django.shortcuts import render, redirect
from .models import Project, Skill, Contact, Blog
from .forms import ContactForm

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
        'blogs': blogs,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email, message=message)
            # You can add a success message or redirect here
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')


def blog(request):
    blogs = Blog.objects.filter(status=1).order_by('-published_date')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'blog_detail.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def skills(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request, 'skills.html', context)

def about(request):
    return render(request, 'about.html')
