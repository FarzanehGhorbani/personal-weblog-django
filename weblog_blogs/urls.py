from django.urls import path
from .views import (BlogsList,
                    CategoryList,
                    blogs_categories_partial,
                    blogs_tags_partial,
                    TagsList,
                    blogs_detail,
                    blogs_popular_blogs)

app_name = 'blogs'

urlpatterns = [
    path('', BlogsList.as_view(), name='list'),
    path('<slug>/<title>', blogs_detail, name='info'),
    path('<category_name>', CategoryList.as_view(), name='categories'),
    path('search-<slug>/', TagsList.as_view(), name='search'),
    path('blogs_categories_partial/', blogs_categories_partial, name='category'),
    path('blogs_tags_partial/', blogs_tags_partial, name='tag'),
    path('blogs_popular_blogs/', blogs_popular_blogs, name='popular_blog'),
]
