from django.shortcuts import render,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from .settings import EMAIL_HOST_USER


def my_home(request):
    import socket
    import getpass
    from uuid import getnode as get_mac
    import re, uuid
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    name = request.GET.get('name')
    email= request.GET.get('email')
    subject= request.GET.get('subject')
    message= request.GET.get('textarea')
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    user = getpass.getuser()
    send_mail(str(subject),
              ( str(message) + ' \n\nPerson name: ' + str(name) + '\nMail :' + str(email)+'\n local ip:'+local_ip+'\n mac address: '+str(':'.join(re.findall('..', '%012x' % uuid.getnode())))+"\nPc username is: "+str(user)), EMAIL_HOST_USER,
                  ['mehedibinhafiz@gmail.com'], fail_silently=False)
    return render(request, 'My_Home.html')



