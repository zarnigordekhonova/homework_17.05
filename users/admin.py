from django.contrib import admin
from .models import CustomUser
# Register your models here.

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username' ,'first_name', 'last_name', 'is_staff', 'is_active')
#     list_filter = ['is_staff', 'is_superuser', 'username']

# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
