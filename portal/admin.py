from django.contrib import admin

# Register your models here.
from .models.book import Book
from .models.course import Course
from .models.event import Event
from .models.post import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "subtitle", "author")
    list_display = ("title", "author", "publication_date", "status")
    list_filter = ("publication_date", "status", "category")
    prepopulated_fields = {"slug": ("title",)}


class EventAdmin(admin.ModelAdmin):
    search_fields = ("title", "description", "address")
    list_display = ("title", "address", "start_date", "end_date")
    list_filter = ("start_date", "end_date", "status")
    prepopulated_fields = {"slug": ("title",)}


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "authors", "isbn", "publisher", "release_year")
    list_filter = ("release_year", "category")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Course)
admin.site.register(Book, BookAdmin)
