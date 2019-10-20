# users/urls.py
from django.urls import path
from .import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('nada/',views.prueba_visual, name='prueba_visual')
]