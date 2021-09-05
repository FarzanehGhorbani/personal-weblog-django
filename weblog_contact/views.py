from django.shortcuts import render
from weblog_contact.forms import ContactForm
from weblog_contact.models import ContactWay
from weblog_content.models import Content


def contact_page(request):
    new_contact = None
    # Comment posted
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Create Comment object but don't save to database yet
            if len(contact_form.cleaned_data.get('name')) < 4:
                contact_form.add_error('name', 'نام شما نمی تواند کمتر از 3 کارکتر باشد')
            else:
                new_contact = contact_form.save(commit=False)

                new_contact.save()
                contact_form = ContactForm()
    else:
        contact_form=ContactForm()

    content=Content.objects.last()
    context = {'contact_form': contact_form,'new_contact':new_contact,'content':content.contact_content}
    return render(request, 'contact/contact_us.html', context)

def contactway_contact(request):
    contact_way=ContactWay.objects.last()
    context={'contact_way':contact_way}
    return render(request,'contact/contact_way_in_contact_us_page.html',context)
