from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from dogs.models import Dog
from dogs.models import Breed
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.validators import MinValueValidator, MaxValueValidator
 

def index(request):
    return HttpResponse("Hello, world. You're at the dogs index.")
 

class BreedSerializer(serializers.ModelSerializer):
    DOG_SIZES = [
        ("T", "Tiny"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
 
    class Meta:
        model = Breed
        fields = '__all__'
 
    name = serializers.CharField(max_length=30)
    friendliness = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    trainability = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    sheddingamount = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    exerciseneeds = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
 
class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
 
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    gender = serializers.CharField(max_length=8)
    color = serializers.CharField(max_length=8)
    favoritefood = serializers.CharField(max_length=30)
    favoritetoy = serializers.CharField(max_length=30)
 
    def post(self, validated_data):
        return Dog(**validated_data)



class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
 
   
   
class BreedViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
   
 
 