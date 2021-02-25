# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.object.email)
        if not self.object.email.endswith('@reactorlabs.studio'):
            # form.add_error("title", "This Question already exist")
            return self.form_invalid(form)
        # self.object.created_by_user = self.request.user
        self.object.save()
        return super().form_valid(form)
