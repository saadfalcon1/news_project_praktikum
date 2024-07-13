from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm


# Create your views here.
def news_list(request):
    news_list = News.published.all()
    context = {'news_list': news_list}
    return render(request, 'news/news_list.html', context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {'news': news}
    return render(request, 'news/news_detail.html', context)


# def indexView(request):
#     news_list = News.published.all().order_by('-publish_time')
#     categories = Category.objects.all()
#     context = {'news_list': news_list, 'categories': categories}
#     return render(request, 'news/index.html', context)


class IndexView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')
        return context


class ContactView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Rahmat </h2>")
        context = {'form': form}
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'news/about.html'


