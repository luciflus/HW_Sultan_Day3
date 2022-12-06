import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Client, Credit, Account
from django.views import generic

class ClientsView(generic.ListView):
    model = Client
    template_name = 'list_clients.html'
    context_object_name = 'client_list'


class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = 'client'
    pk_url_kwarg = 'id'
