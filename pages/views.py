from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.


class HomePageView(CreateView):
    template_name = 'home.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")


class AboutPageView(TemplateView):
    template_name = 'about.html'
