from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'shipping_cost', 'status', 'created_at')
    list_filter = ('status',)