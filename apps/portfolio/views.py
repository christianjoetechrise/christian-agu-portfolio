from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse, Http404
import resend

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def services(request):
    return render(request, 'portfolio/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        subject = f'Portfolio Contact Message from {name}'

        email_message = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        resend.api_key = settings.RESEND_API_KEY

        resend.Emails.send({
            "from": f"Christian Agu Portfolio <{settings.DEFAULT_FROM_EMAIL}>",
            "to": [settings.CONTACT_EMAIL],
            "subject": subject,
            "text": email_message,
        })

        return render(
            request,
            'portfolio/contact.html',
            {'success': True}
        )

    return render(request, 'portfolio/contact.html')

def resume(request):
    return render(
        request,
        'portfolio/resume.html',
        {'MEDIA_URL': settings.MEDIA_URL}
    )
    
def download_cv(request):
    cv_path = settings.MEDIA_ROOT / "documents" / "Christian_Agu_CV.pdf"

    if not cv_path.exists():
        raise Http404("CV file not found.")

    return FileResponse(
        open(cv_path, "rb"),
        as_attachment=True,
        filename="Christian_Agu_CV.pdf",
        content_type="application/pdf",
    )