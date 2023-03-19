from django.contrib import admin
from .models import myUser
from .models import Contact
# Register your models here.
admin.site.register(myUser)
admin.site.register(Contact)