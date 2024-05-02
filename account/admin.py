from django.contrib import admin

# Register your models here.
from .models import Project, Skill, Contact, Blog


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date')
    list_filter = ('status', 'created_date', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Blog, BlogAdmin)
