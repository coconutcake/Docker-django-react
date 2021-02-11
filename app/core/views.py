from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect,reverse
from django.views.generic.base import RedirectView
import django
import os
class MainView(TemplateView):
    template_name = "core/welcome.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['django_version'] = django.get_version()
        context['pip_packages'] = os.popen("pip freeze").read().split("\n")
        return context