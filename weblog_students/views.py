from weblog_about_us.models import AboutUs
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from weblog_content.models import Content
from .models import Students
# Create your views here.

class StudentListView(ListView):
    queryset = Students.objects.filter(active=True)
    template_name = 'students/students.html'
    paginate_by = 9

    def get_context_data(self, *args, **kwargs):
        context=super(StudentListView, self).get_context_data(*args,**kwargs)
        content=Content.objects.last()
        context['content']=content
        context['about_us']=AboutUs.objects.last()
        return context

class StudentsDetailView(DetailView):
    queryset = Students.objects.all()
    template_name = 'students/students_info.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            student_info = Students.objects.get(slug=slug)
        except Students.DoesNotExist:
            raise Http404("research does not exists ...")
        except Students.MultipleObjectsReturned:
            qs = Students.objects.filter(slug=slug)
            student_info = qs.first()

        return student_info

    def get_context_data(self, *args, **kwargs):
        context=super(StudentsDetailView, self).get_context_data(*args,**kwargs)
        context['about_us']=AboutUs.objects.last()
        return context




