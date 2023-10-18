from django.contrib import admin
from django.urls import path, include, re_path
from dogs import views
from dogapi import controllers
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from .controllers import DogList, DogDetails, BreedList, BreedDetails


router = routers.SimpleRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'breed', views.BreedViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
urlpatterns = format_suffix_patterns(urlpatterns)