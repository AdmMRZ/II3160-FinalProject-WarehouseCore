# main/admin.py (REPO 1)
from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    # Hapus 'shipping_cost' dari sini karena di models.py gak ada field itu
    list_display = ('id', 'name', 'status', 'created_at') 
    list_filter = ('status',)
    search_fields = ('name',)