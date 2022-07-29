from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Mailing, Client, Message

from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.models import User, Group
from rest_framework import viewsets


def MailingViewSet(request):
    queryset = Mailing.objects.all()
    return render(request, 'services/list.html',{'queryset': queryset})



def ClientViewSet(request):

    return render(request, 'services/list.html')



def MessageViewSet(request):
    return render(request, 'services/list.html')
