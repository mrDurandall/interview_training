from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    extra_context = {'title': 'Главная'}
    template_name = 'common/index.html'
