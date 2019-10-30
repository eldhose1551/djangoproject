from django.contrib import admin
from . models import Blog, Author


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_on', 'created_on')
    search_fields = ['title', 'content']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)

