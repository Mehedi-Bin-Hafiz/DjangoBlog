from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect

def my_home(request):
    print(request.POST)
    name = request.POST.get('name')
    email= request.POST.get('email')
    subject= request.POST.get('subject')
    textarea= request.POST.get('textarea')

    print(name)

    return render(request,'My_Home.html')