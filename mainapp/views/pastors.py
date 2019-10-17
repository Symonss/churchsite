from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from mainapp.forms import PastorSignupForm
from django.shortcuts import render
from ..models import User,Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from ..decorators import pastor_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class PastorSignUpView(CreateView):
    model = User
    form_class = PastorSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pastor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pastors_home')

def pastorHome(request):
    staff = User.objects.all()
    return render(request,  'pastor/dashboard1-staff.html', {'staff':staff})

def groupView(request):
    groups = Group.objects.all()
    return render(request, 'pastor/dashboard2-groups.html', {'groups':groups})

class GroupCreateView(CreateView):
    model = Group
    fields = ('name','leader')
    template_name = 'pastor/group_add_form.html'

    def form_valid(self, form): 
        group = form.save(commit=False)
        # tgroup.added_by = self.request.user
        group.save()
        messages.success(self.request, 'Group Succesfully Created!')
        if self.request.user.is_pastor:
            return redirect('pastors_home')

        else:
            return redirect('index')

        