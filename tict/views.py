from django.shortcuts import redirect
from django.contrib.auth.forms import PasswordResetForm
from django.views.generic import CreateView

from .forms import RegistrationForm
from .models import User

class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.set_password(User.objects.make_random_password())
        obj.save()

        reset_form = PasswordResetForm(self.request.POST)
        reset_form.is_valid()
        opts = {
        'use https':self.rquest.is_secure()
        'email_template_name':'registration/verification.html',
        'subject_template_name':'registration/verification_subject.txt',
        'request':self.request
        }
        reset_form.save(**opts)
        return redirect('tict:register-done')

# Create your views here.
