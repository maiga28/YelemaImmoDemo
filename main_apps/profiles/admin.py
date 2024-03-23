from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'phone_number', 'location')
    search_fields = ['user__username', 'user__email', 'phone_number', 'location']
    list_filter = ('date_of_birth',)

admin.site.register(Profile, ProfileAdmin)

