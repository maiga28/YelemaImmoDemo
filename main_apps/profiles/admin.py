
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 's_name', 'date_joined', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 's_name', 'adresse', 'numero_telephone', 'bio', 'date_of_birth', 'phone_number', 'location', 'profile_picture','cover_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 's_name', 'adresse', 'numero_telephone', 'bio', 'date_of_birth', 'phone_number', 'location', 'profile_picture','cover_picture','password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 's_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)