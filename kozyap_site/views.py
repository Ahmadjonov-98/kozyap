from django.shortcuts import render
from django.views.generic import TemplateView

from kozyap_site.models import About, Partner


class IndexPageView(TemplateView):
    template_name = 'app/index.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.all()

        context['abouts'] = about

        return context


class CommunicatePageView(TemplateView):
    template_name = 'app/communication.html'


class FriendPageView(TemplateView):
    template_name = 'app/friends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partners = Partner.objects.all()

        context['partners'] = partners

        return context


class GalleryPageView(TemplateView):
    template_name = 'app/gallery.html'


class ReferencePageView(TemplateView):
    template_name = 'app/reference.html'
