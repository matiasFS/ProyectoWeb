from django.urls import path
from django.conf.urls.static import static
from Blog import views

urlpatterns = [
    path('', views.blog, name="Blog"),
]