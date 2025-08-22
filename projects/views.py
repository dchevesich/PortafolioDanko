from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    f'Mensaje de contacto de {name}',
                    f'De: {email}\n\nMensaje:\n{message}',
                    settings.EMAIL_HOST_USER,  
                    [settings.EMAIL_RECEIVER],  
                    fail_silently=False,
                )
                
                return redirect('home') 
            except Exception as e:
                
                print(f"Error al enviar correo: {e}")
    else:
        form = ContactForm()

    return render(request, 'index.html', {'projects': projects, 'form': form})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})