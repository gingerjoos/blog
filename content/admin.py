from content.models import Post,Comment
from django.contrib import admin

#admin.site.register(Comment)
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['title','body']}),
        ('Meta',{'fields':['is_published','comments_allowed','url','author'],'classes':['collapse']}),
    ]

    list_display = ('title','created_on','updated_on')
    list_filter = ('created_on','updated_on','is_published')
    search_fields = ['title']
    date_hierarchy = 'created_on'


admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','name','created_on')
    list_filter = ('created_on','updated_on','is_approved')
    date_hierarchy = 'created_on'

admin.site.register(Comment,CommentAdmin)
