from django.contrib import admin

# Register your models here.
from .models import Client, Token

# Create model admins

class ClientAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'status', 'user', 'updated_at', 'created_at')
    search_fields = ('key', 'status')


admin.site.register(Client, ClientAdmin)
admin.site.register(Token, TokenAdmin)
