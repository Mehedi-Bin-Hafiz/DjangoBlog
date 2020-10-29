from django.shortcuts import render,HttpResponse

# Create your views here.

from .models import Post

def post_home(request):
    return HttpResponse("<h1>This is home</h1>")

def post_detail(request):

    context = {
        'title': "details",
        'content': "this is post details"
    }
    return render(request, "index.html", context)
def post_list(request):
    qs = Post.objects.all()
    context = {
        'title': "list",
        'object_list': qs
    }
    return render(request, "index.html", context)
def post_delete(request):
    return HttpResponse("<h1>This is delete</h1>")