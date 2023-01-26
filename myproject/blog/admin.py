from django.contrib import admin
from .models import Blog,Author,Comment
from django.template.defaultfilters import truncatechars

admin.site.register(Author)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('get_description','commented_date')
    def get_description(self,obj):
        return obj.comment_content[:75]
    
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)



