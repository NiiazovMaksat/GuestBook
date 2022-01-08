from django.contrib import admin
from webapp.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated_at', 'status']
    list_filter = ['status']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'updated_at', 'status']

admin.site.register(Book, BookAdmin)