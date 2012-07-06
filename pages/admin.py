from models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}

admin.site.register(Page,PageAdmin)
