from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from mainapp.forms import ElderSignupForm
from django.shortcuts import render
from ..models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from ..decorators import elder_required
from django.contrib.auth.decorators import login_required

class ElderSignUpView(CreateView):
    model = User
    form_class = ElderSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Elder'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

