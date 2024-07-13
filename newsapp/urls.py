from django.urls import path
from .views import news_list, news_detail, IndexView, ContactView, AboutView
urlpatterns = [
    path('contact-page/', ContactView.as_view(), name='contact_page'),
    path('', IndexView.as_view(), name='index'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail,  name='news_detail_page'),
    path('about/', AboutView.as_view(), name='about_page'),
]
