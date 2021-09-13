from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from validate_email import validate_email
from weblog_blogs.forms import CommentForm
from weblog_blogs.models import Blogs, Comment
from weblog_blogs_Tags.models import Tags
from weblog_blogs_category.models import Categories
from weblog_content.models import Content
from weblog_about_us.models import AboutUs

class BlogsList(ListView):
    template_name = 'blogs/blogs_list.html'

    paginate_by = 9

    def get_queryset(self):
        return Blogs.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BlogsList, self).get_context_data(*args, **kwargs)
        content = Content.objects.last()
        context['content'] = content
        context['about_us']=AboutUs.objects.last()
        context['home_url'] = "active"
        return context


def blogs_detail(request, slug, title):
    about_us:AboutUs=AboutUs.objects.last()
    blog: Blogs = get_object_or_404(Blogs.objects.annotate(num_comment=Count('comments')), slug=slug)
    blog.count_comment = Comment.objects.all().count()
    blog.save()
    comments = blog.comments.all()
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            if len(comment_form.cleaned_data.get('name')) < 4:
                comment_form.add_error('name', 'نام شما نمی تواند کمتر از 3 کارکتر باشد')
            elif validate_email(comment_form.cleaned_data.get('name'), verify=True):
                comment_form.add_error('emil', 'ایمیل شما معتبر نیست')
            else:
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.blog = blog
                # Save the comment to the database
                new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'blogs/blogs_info.html', {'object': blog,
                                                     'comments': comments,
                                                     'new_comment': new_comment,
                                                     'comment_form': comment_form,
                                                     'about_us':about_us })
                                                     


class CategoryList(ListView):
    template_name = 'blogs/blogs_list.html'
    paginate_by = 9

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        category = Categories.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('این صفحه یافت نشد')
        return Blogs.objects.get_by_categories(category_name)


def blogs_categories_partial(request):
    categories = Categories.objects.annotate(num_blog=Count('blogs')).order_by('-num_blog')
    context = {'categories': categories}
    return render(request, 'blogs/blogs_category.html', context)


def blogs_tags_partial(request):
    tags = Tags.objects.all()
    context = {'tags': tags}
    return render(request, 'blogs/blogs_tags.html', context)


def blogs_popular_blogs(request):
    blogs = Blogs.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:3]
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs_popular.html', context)


class TagsList(ListView):
    template_name = 'blogs/blogs_list.html'
    paginate_by = 9

    def get_queryset(self):
        tag_slug = self.kwargs.get('slug')
        return Blogs.objects.filter(tags__slug__iexact=tag_slug).distinct()
