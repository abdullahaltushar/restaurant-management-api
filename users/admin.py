from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm

    list_display = ("email", "name", "is_admin", "is_staff", )
    list_filter = ("is_admin", "is_staff")
    search_fields = ("email", "name")

    ordering = ("email",)
    filter_horizontal = ()

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("is_admin", "is_staff" )}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2","is_admin", "is_staff"),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)
