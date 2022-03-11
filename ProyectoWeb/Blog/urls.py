from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('category/<int:category_id>', views.category, name="category"),

]