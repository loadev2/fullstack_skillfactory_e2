from django.shortcuts import render
from django.views.generic import ListView
from common.models import Message

from django.core.mail import send_mail
from django.conf import settings
import threading
from datetime import datetime


class ListMessage(ListView):
    model = Message
    context_object_name = 'msgs'
    template_name = 'list.html'
    queryset = Message.objects.order_by('-id')[:10]


def add_email(request):
    if request.method == 'POST':
        message = request.POST['message']
        sec = int(request.POST['time'])
        print(message)
        msg = Message(title="Msg - {}".format(datetime.now()), body=message, status=2)
        msg.save()
        t = threading.Timer(sec, send_email, args=(message, msg))
        t.start()
        print('Ending tread')

    return render(request, 'index.html', {})

def send_email(message, msg):
    msg.status=1
    msg.save()
    send_mail('Contact Form',
                message,
                settings.EMAIL_HOST_USER,
                ['loadev@gmail.com'],
                fail_silently=False)