from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm
# Create your views here.

from .models import Post

def post_home(request):
    return HttpResponse("<h1 style='text-align: center; color: red;'>Page will be updated</h1>")

def post_detail(request, id = None): #id technically is a keyword args
    instance = get_object_or_404(Post, id = id)
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

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)  # this instance is related to Post model.
        instance.save()
        messages.success(request,"successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'mytitle': 'Create Post',
        'form':form
    }

    return render(request,'create_post.html',context)

def post_update(request, id = None):
    instance = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "successfully edited",extra_tags='some_tag')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title': instance.title,
        'instance': instance,
        'form':form
    }
    return render(request, "create_post.html", context)