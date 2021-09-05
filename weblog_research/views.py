from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from weblog_content.models import Content
from .models import CurrentTopics, ResearchGrants, ResearchPartners
from meta.repeatable_code import my_grouper


def research_page(request):
    content=Content.objects.last()
    current_topics = list(my_grouper(2, CurrentTopics.objects.active()))
    research_grants = ResearchGrants.objects.all()
    research_collaborators = ResearchPartners.objects.active()

    context = {
        'current_topics': current_topics,
        'research_grants': research_grants,
        'research_collaborators': research_collaborators,
        'content':content
    }
    return render(request, 'research/research.html', context)


class ResearcherList(ListView):
    template_name = 'research/researcher.html'
    queryset = ResearchPartners.objects.active()
    paginate_by = 9


class ResearcherDetailView(DetailView):
    queryset = ResearchPartners.objects.active()
    template_name = 'research/researcher_info.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            research_info = ResearchPartners.objects.get(slug=slug)
        except ResearchPartners.DoesNotExist:
            raise Http404("research does not exists ...")
        except ResearchPartners.MultipleObjectsReturned:
            qs = ResearchPartners.objects.filter(slug=slug)
            research_info = qs.first()

        return research_info
