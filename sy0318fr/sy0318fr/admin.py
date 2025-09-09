from django.contrib import admin
from .models import Memory

class MemoryAdmin(admin.ModelAdmin):
    list_display = ('photo', 'place', 'description')

admin.site.register(Memory)