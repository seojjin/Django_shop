from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Item, Category, Tag, Company, Comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Tag, TagAdmin)


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Company, CompanyAdmin)

admin.site.register(Comment)

admin.site.register(Item, MarkdownxModelAdmin)
