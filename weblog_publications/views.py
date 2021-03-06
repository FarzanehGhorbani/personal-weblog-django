from collections import defaultdict
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from weblog_about_us.models import AboutUs
from weblog_content.models import Content
from .forms import CommentForm
from .models import Publications, Comment


def publications_page(request):
    about_us=AboutUs.objects.last()
    content=Content.objects.last()
    top_books = Publications.objects.filter(active_for_top=True).order_by('-publish_date', '-id')[:3]
    all_books = Publications.objects.order_by('-publish_date').all()
    release_list = defaultdict(list)

    for y in all_books:
        release_list[y.publish_date.year].append(y)

    books = []
    for key, value in release_list.items():
        books.append(value)


    context = {
        'about_us':about_us,
        'top_books': top_books,
        'all_books': books,
        'content':content
    }
    return render(request, 'publications/publications.html', context)


def book_detail(request, slug, name):
    about_us=AboutUs.objects.last()
    book: Publications = get_object_or_404(Publications.objects.all(), slug=slug)
    book.count_comment = Comment.objects.get_active_comments(book).count()
    book.save()
    comments = book.comments.filter(active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            if len(comment_form.cleaned_data.get('name')) < 4:
                comment_form.add_error('name', 'نام شما نمی تواند کمتر از 3 کارکتر باشد')

            else:
                new_comment = comment_form.save(commit=False)
                # Assign the current post to the comment
                new_comment.book = book
                # Save the comment to the database
                new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'publications/book_info.html', {'object': book,
                                                            'about_us':about_us,
                                                           'comments': comments,
                                                           'new_comment': new_comment,
                                                           'comment_form': comment_form})
