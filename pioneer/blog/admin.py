from django.contrib import admin
from blog.models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    list_fields = ['title', 'content']
    prepopulated_fields ={'slug':('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)