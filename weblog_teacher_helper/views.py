from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ResumeForm
from django.http import HttpResponseRedirect

from .models import TeacherHelper


def upload_file(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('Okkkkkkkkkkkkkk')
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('teaching'))
    else:
        form = ResumeForm()
    return render(request, 'teacher_helper/teacher_helper.html', {'form': form})
