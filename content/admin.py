from content.models import Post,Comment
from django.contrib import admin

#admin.site.register(Comment)
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
        (None,{'fields':['title','body']}),
        ('Category',{'fields':['category']}),
        ('Meta',{'fields':['is_published','comments_allowed','slug','author']}),
    ]

    list_display = ('title','created_on','updated_on')
    list_filter = ('created_on','updated_on','is_published')
    search_fields = ['title']
    date_hierarchy = 'created_on'

    def formfield_for_foreignkey(self,db_field,request,**kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        return super(PostAdmin,self).formfield_for_foreignkey(db_field,request,**kwargs)


admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body','name','created_on')
    list_filter = ('created_on','updated_on','is_approved')
    date_hierarchy = 'created_on'

admin.site.register(Comment,CommentAdmin)
