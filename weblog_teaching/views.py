from django.shortcuts import render
from weblog_about_us.models import AboutUs
from weblog_content.models import Content
from weblog_teaching.models import Teaching, LessonList


def teaching_page(request):
    about_us = AboutUs.objects.last()
    content=Content.objects.last()
    teaching = Teaching.objects.all()
    lesson_list = LessonList.objects.all()
    context = {
        'about_us':about_us,
        'teaching': teaching,
        'lesson_list': lesson_list,
        'content':content
    }
    return render(request, 'teaching/teaching.html', context)