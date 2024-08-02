from django.contrib import admin

# Register your models here.

from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    prepopulated_fields = {"slug": ("first_name", "last_name")}
    
admin.site.register(Member, MemberAdmin)