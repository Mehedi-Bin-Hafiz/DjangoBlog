from django.shortcuts import render,HttpResponse, get_object_or_404

# Create your views here.

from .models import Post

def post_home(request):
    return HttpResponse("<h1>This is home</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id = 1)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, "post_detail.html", context)
def post_list(request):
    qs = Post.objects.all()
    context = {
        'title': "list",
        'object_list': qs
    }
    return render(request, "index.html", context)
def post_delete(request):
    return HttpResponse("<h1>This is delete</h1>")