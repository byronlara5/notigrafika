"""notigrafika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from post.views import Home, Categories, Entry_detail, Tags

from post.models import Post, Category

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import DetailView, ListView, TemplateView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home, name='home'),
    url(r'^(?P<slug>[\w-]+)/$', Entry_detail, name='entry_detail'),
    url(r'^sections/(?P<category_slug>[-\w]+)/$', Categories, name='categories'),
    url(r'^tags/(?P<tag_slug>[-\w]+)/$', Tags, name='tags'),
    url(r'^page/about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^legal/privacy-policy/', TemplateView.as_view(template_name='privacy.html'), name='privacy'),
    url(r'^legal/terms-of-use/', TemplateView.as_view(template_name='termsofuse.html'), name='terms-of-use'),



    #3rd Party
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
