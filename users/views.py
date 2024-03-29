from django.shortcuts import render

# Create your views here.

# users/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def prueba_visual(request):
    return render(request,'page/nueva.html' )