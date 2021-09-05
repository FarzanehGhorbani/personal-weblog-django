from django.shortcuts import render

# Create your views here.
from weblog_content.models import Content
from weblog_teaching.models import Teaching, LessonList


def teaching_page(request):
    content=Content.objects.last()
    teaching = Teaching.objects.all()
    lesson_list = LessonList.objects.all()
    context = {
        'teaching': teaching,
        'lesson_list': lesson_list,
        'content':content.teaching_content
    }
    return render(request, 'teaching/teaching.html', context)