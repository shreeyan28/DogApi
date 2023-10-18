from django.contrib import admin
from dogs.models import Dog
from dogs.models import Breed

# Register your models here.
class DogAdmin(admin.ModelAdmin):
    pass 


admin.site.register(Dog, DogAdmin)


class DogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Breed, DogAdmin)