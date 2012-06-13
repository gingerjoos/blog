from taxonomy.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("term",)}
    list_display = ['term','parent']

admin.site.register(Category,CategoryAdmin)
