from django.shortcuts import render
from weblog_contact.models import ContactWay
from weblog_about_us.models import AboutUs
from weblog_content.models import Content
def footer(request):
    contact=ContactWay.objects.last()
    about_us=AboutUs.objects.last()
    content=Content.objects.last()
    context={
        'contact':contact,
        'about_us':about_us,
        'footer_content':content.footer_content}
    return render(request,'shared/Footer.html',context)

def header(request):
    context={}
    return render(request,'shared/Header.html',context)