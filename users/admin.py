from django.contrib import admin
from .models import CustomUser, PasswordReset
# Register your models here.


admin.site.register(PasswordReset)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """ list display shows selected product details """
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'date_joined']
