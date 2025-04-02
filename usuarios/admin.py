from django.contrib import admin
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UsersInLine(admin.StackedInline):
    model = Usuarios
    can_delete = False
    verbose_name_plural = 'Usuarios'

class CustomUserAdmin(UserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UsersInLine]
        return super(UserAdmin, self).change_view(*args, **kwargs)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)