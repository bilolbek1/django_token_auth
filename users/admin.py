from django.contrib import admin

from .models import CustomUser
from rest_framework.authtoken.models import Token

class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']

admin.site.register(CustomUser, UserAdmin)


