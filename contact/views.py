from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['petersenmark92@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Header Error')
            return redirect('send')
    return render(request, 'contact/contact.html', {'form' : form})

def sendView(request):
    return render(request, 'contact/send.html')