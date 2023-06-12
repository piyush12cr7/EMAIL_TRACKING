from django.shortcuts import render, redirect
from .forms import EmailForm
from .models import Email
from django.core.mail import send_mail
import logging
logger = logging.getLogger('django')


def email_create(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save()
            subject = email.subject
            message = email.content
            recipient_list = [email.recipient]
            from_email = 'piyush12cr7@gmail.com'  
            send_mail(subject, message, from_email, recipient_list) 
            email.status = 'Sent'  # Update the status
            email.save()
            logger.debug('Email sent successfully: %s', email.subject)
            return redirect('email_list')
        else:
            form = EmailForm()
    return render(request, 'email/create.html', {'form': form})

def email_list(request):
    emails = Email.objects.all()
    return render(request, 'email/list.html', {'emails': emails})