from django.urls import path
from .views import RegisterView, log_out, log_in

urlpatterns = [
    path('', RegisterView.as_view(), name="authentication"),
    path('logout', log_out, name="logout"),
    path('login', log_in, name="login"),
]