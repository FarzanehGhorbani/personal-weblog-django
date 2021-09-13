from collections import defaultdict
from weblog_about_us.models import AboutUs
from django.db.models import Count
from django.shortcuts import render
from extensions.utils import date
from meta.repeatable_code import my_grouper
from weblog_blogs.models import Blogs
from weblog_publications.models import Publications
from .models import HonorsAndAwards, Education


# Create your views here.

def home_page(request):
    about_us=AboutUs.objects.last()
    education = Education.objects.all()
    honor: HonorsAndAwards = HonorsAndAwards.objects.order_by('date').all()
    educations = my_grouper(2, education)
    books = Publications.objects.filter(active_for_top=True).order_by('-id')[:6]
    blogs = Blogs.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:3]
    honor_year=set()
    release_list = defaultdict(list)

    for y in honor:
        release_list[y.date.year].append(y)
        honor_year.add(date(y.date))

    honors = []
    for key, value in release_list.items():
        honors.append(value)
    
    
    context = {
        'about_us':about_us,
        'educations': educations,
        'honors': honors,
        'honor_year':honor_year,
        'books':books,
        'blogs':blogs
    }
    return render(request, 'about_us/home.html', context)
