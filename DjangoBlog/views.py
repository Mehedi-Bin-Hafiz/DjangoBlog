from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect

def my_home(request):
    return render(request,'My_Home.html')