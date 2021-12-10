from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

import datetime
# Create your views here.


class HomePageView(CreateView):
    template_name = 'pages/home.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the current year
        current_date = datetime.datetime.now()
        context['year'] = current_date.year
        return context


class VimCheatSheet(TemplateView):
    template_name = 'pages/vimcheatsheet.html'


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")


class AboutPageView(TemplateView):
    template_name = 'about.html'
