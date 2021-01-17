from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Role

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'first_name', 'last_name', 'email','is_staff', 'is_approved', 'zoom')
    search_fields = ('username', 'email',)
    readonly_fields=()
    filter_horizontal = ()

    # def get_role (self, obj):
    #     return obj.role.name

    # get_role.short_description = "Role"
    # get_role.admin_order_field = "role"

admin.site.register(CustomUser, CustomUserAdmin)


class Role_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    readonly_fields=()
    filter_horizontal = ()

admin.site.register(Role, Role_Admin)