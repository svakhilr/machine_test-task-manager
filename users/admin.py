from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username","name", "is_staff", "is_active",)
    list_filter = ("username","name", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "name","password","role")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "name","username" ,"password1", "password2","role" ,"is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("name",)
    ordering = ("name",)
