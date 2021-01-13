from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Track, ImageGallery, Video_Gallery, Signature, Graphics

# Create your views here.

def home(request):
    gallery = ImageGallery.objects.all()
    sign = Signature.objects.all()
    single = Track.objects.get(pk=5)
    #mainpic = Track.objects.filter(pk=3)
    context = {
        'gallery':gallery,
        'single':single,
        'sign':sign,
    }
    return render(request, 'seyi_music/index.html',context)

def about(request):
    gallery = ImageGallery.objects.all()
    context = {
        'title':'About',
        'gallery':gallery
        }
    return render(request,'seyi_music/about.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_subject = form.cleaned_data['subject']
            sender_message = form.cleaned_data['message']
            message = "Hello ! \n\n {} just sent you a mail. \n\n MESSAGE: {}. Reply to {}".format(sender_name, 
                sender_message,(sender_email))
             
            send_mail(sender_subject, message, sender_email, ['sdamilare420@gmail.com'],fail_silently=False)
            messages.success (request, f'Thank you for contacting us! We will get back to you shortly.')
            return redirect ('contact')
    else:
        form = ContactForm()
    context =  {'title':'Contact','form': form}
    return render(request, 'seyi_music/contact.html',context)

def tracks(request):
    tracks = Track.objects.all()
    paginator= Paginator(tracks, 3) #shows 3 tracks per page
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    vids = Video_Gallery.objects.all()
    context = {
        'title':'Tracks', 
        'tracks':tracks, 
        'vids':vids,
        'page_obj':page_obj,
     }
    return render(request, 'seyi_music/track.html',
)

def services(request):
    graphics=Graphics.objects.all()
    context = {'title':'Services', 'graphics':graphics}
    return render(request, 'seyi_music/services.html',context)


