from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_fullname', 'user_company', 'email', 'last_login')
    list_filter = ('last_login',)

admin.site.register(User, UserAdmin)
