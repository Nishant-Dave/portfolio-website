from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Project, Post


def home(request):
    projects = Project.objects.all().order_by('order')
    posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3] # Show a preview

    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'core/home.html', context)

def blog_list(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {'posts': posts}
    return render(request, 'core/blog_list.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    recent_posts = Post.objects.filter(is_published=True).exclude(id=post.id).order_by('-created_at')[:5]
    
    context = {
        'post': post,
        'recent_posts': recent_posts
    }
    return render(request, 'core/blog_detail.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Send email
        subject = f"Portfolio Contact Form: {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                subject,
                body,
                email, # from email
                [settings.ADMIN_EMAIL], # to email (must be configured in settings)
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
        except Exception as e:
            # In a real app, you'd want to handle this gracefully and show an error message
            print(f"Error sending email: {e}")

        return redirect('core:home')
    
    return redirect('core:home')
