from django.urls import path
from .views import SignUpView, staff_list

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('staff/', staff_list, name='staff_list'),
]
