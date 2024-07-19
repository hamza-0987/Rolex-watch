from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from product.models import Product
from testimonial.models import Testimonial
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
import socket
import logging
from django.http import HttpResponse


def home(request):
    products = Product.objects.all()
    for a in products:
        print(a.title)
    
   

    testimonial=Testimonial.objects.all()


   # for a in products:
        #print(a.price)
        #print(a.image)
        #print(a.title)

    #for b in testimonial:
        #print(b.name)
        #print(b.role)
        #print(b.image)
        #print(b.testimonial_date)
        #print(b.testimonial_text)

#create a logic that filters on the basis of title and then after filter goes to its previous state 

    if request.method =="GET":
        products_info =request.GET.get("servicename")
        print(products_info)
        if products_info != None:
            products = Product.objects.filter(title__icontains=products_info)
            products_info=""

        paginator = Paginator(products,1)  
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    
    data = {
       
        'products': page_obj,
        'testimonial':testimonial,
    }

    try:
        # Example of a DNS resolution attempt
        ip = socket.gethostbyname('example.com')
        logging.info(f'IP address of example.com: {ip}')
    except socket.gaierror as e:
        logging.error(f'DNS resolution failed: {e}')
        return HttpResponse("DNS resolution failed", status=500)

    
    subject = 'Test Email from Django'
    message = 'This is a test email sent from Django.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['certification1290@gmail.com']

    send_mail(subject, message, email_from, recipient_list)
    print("email sent successfully")
    

    return render(request, 'home.html', data)



    
    
def product_details(request,slug):
    product = Product.objects.get(product_slug=slug)
    print (id)
    return render(request, 'product_details.html', {'product': product})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
             
    else:
        form = ContactForm()
    
    return render(request, 'contact_form.html', {'form': form})

# views.py

# views.py or any other appropriate place in your project




    

# views.py


















