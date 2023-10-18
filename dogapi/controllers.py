#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import *
from django.contrib.auth import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
#from django.shortcuts import render_to_response
from django.template import RequestContext
#from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import *

# Import models
from django.db import models
from django.contrib.auth.models import *
#from api.models import *

#REST API
from rest_framework import viewsets, filters, parsers, renderers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.authentication import *
from rest_framework import serializers

#filters 
#from filters.mixins import *

#from api.pagination import *
from rest_framework import generics

import json, datetime, pytz
from django.core import serializers
#import requests


def home(request):
   """
   Send requests to / to the ember.js clientside app
   """
   return render_to_response('ember/index.html',
               {}, RequestContext(request))

        
#from .dogs.serializers import DogSerializer, BreedSerializer
from dogs.models import Dog, Breed

#dog
class DogList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Dog.objects.all()
    serializer_class = serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new dog."""
        serializer.save()

class DogDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Dog.objects.all()
    serializer_class = serializers

#Breed 

class BreedList(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Breed.objects.all()
    serializer_class = serializers

    def perform_create(self, serializer):
        """Save the post data when creating a new Breed."""
        serializer.save()

class BreedDetails(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Breed.objects.all()
    serializer_class = serializers
# Testing