from django.views.generic import TemplateView


# Create your views here.


class EmailCaptureView(TemplateView):
    template_name = 'captures/index.html'
