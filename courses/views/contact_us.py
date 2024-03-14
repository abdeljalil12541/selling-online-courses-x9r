from django.shortcuts import redirect, render
from courses.forms.contact_us_form import ContactUsForm
from django.contrib import messages
from django.core.mail import EmailMessage

from django.conf import settings
from django.core.mail import send_mail


def contact_us(request):
    form = ContactUsForm()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ContactUsForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            user = request.user  # Corrected line
            
            email_message = EmailMessage(
                subject=email,  # Subject
                body=message,            # Message
                from_email=settings.EMAIL_HOST_USER,  # Use your Gmail email address here
                to=['sellingonlinecourses@gmail.com'],  # To email
                reply_to=[email]         # Include user's email address in the reply-to header
            )
            email_message.send(fail_silently=False)
            
            messages.success(request, 'The message has been successfully sent.')
            form.save(commit=False)  # Save the form after sending the email
            form.instance.user = user  # Assign user to the form instance
            form.save()  
        
    return render(request, 'courses/contact_us.html', {'form': form})