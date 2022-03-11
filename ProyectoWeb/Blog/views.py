from django.shortcuts import render
from Blog.models import Post, Category
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "Blog/blog.html",{"posts": posts, "categories":categories})

def category(request, category_id):
    category_byId = Category.objects.get(id=category_id)
    posts_filter = Post.objects.filter(categories=category_byId)
    categories_all = Category.objects.all()
    return render(request,"Blog/category.html",{"category_byId":category_byId, "posts_filter":posts_filter, "categories":categories_all})