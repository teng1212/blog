from django.contrib import admin

from .models import Post, Category, Entry
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
