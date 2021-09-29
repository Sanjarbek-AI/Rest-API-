from django.contrib import admin

from profiles_api.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']
    list_filter = ['name']
