from django.contrib import admin

from .models import Blog, Category, Contact, Testimonial


class MainAdmin:
    admin.site.site_header = " BloggersHub.co"
    # admin.site.site_header = "Custom bookstore admin"
    # admin.site.site_title = "Welcome Admin"
    # admin.site.index_title = "Blogger "


class BlogAdmin(admin.ModelAdmin):
    # id = ('id')
    list_display = ('title_tag','add_date','cat')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10
    icon_name = 'library_add'

    class Media:
        js = ('https://cdn.tiny.cloud/1/6h3aiuyj42f0vly6sd11kjl8ok6fw5na0vv4b66ayb3mmriw/tinymce/6/tinymce.min.js',
              'js/main.js')


class CategoryAdmin(admin.ModelAdmin):

    name = 'Categories'
    list_display = ('title', 'image_tag', 'description', 'url')
    list_per_page = 10
    search_fields = ('view_list',)
    icon_name = 'sort'

class Contactadmin(admin.ModelAdmin):
    list_display = ('Name','Email')
    list_per_page = 10
    search_fields = ['Email','Name']
    list_filter = ['Email','Publish_date']
    icon_name = 'message'


class Testimonialadmin(admin.ModelAdmin):
    list_display = ('Name', 'Role', 'Publish_date')
    list_per_page = 10
    search_fields = ['Name']
    list_filter = ['Role']
    icon_name = 'account_circle'

    class Media:
        js = ('https://cdn.tiny.cloud/1/6h3aiuyj42f0vly6sd11kjl8ok6fw5na0vv4b66ayb3mmriw/tinymce/6/tinymce.min.js',
              'js/main.js')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, Contactadmin)
admin.site.register(Testimonial, Testimonialadmin)
