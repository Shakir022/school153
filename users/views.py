from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def staff_list(request):
    staff_users = User.objects.filter(is_staff=True)
    return render(request, 'staff_list.html', {'staff_users': staff_users})
