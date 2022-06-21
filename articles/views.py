from pprint import pprint

from django.shortcuts import render

from articles.models import Article, ArticleSection


def articles_list(request):
    template = 'articles/news.html'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/ #django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    object_list = list(Article.objects.all().order_by(ordering))
    for article in object_list:
        pprint(article)
        for scope in article.scopes.all():
            pprint(scope)
# #
    context = {'object_list': object_list,
}
    return render(request, template, context)

