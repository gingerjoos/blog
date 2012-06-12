from taxonomy.models import Category
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['term','parent']

admin.site.register(Category,CategoryAdmin)
