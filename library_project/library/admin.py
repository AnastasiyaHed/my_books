from django.contrib import admin
from .models import Library, Author, Book


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')  # Отображаем название и город библиотеки


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображаем имя автора


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'library')  # Отображаем название, автора и библиотеку книги


class BookInline(admin.TabularInline):
    model = Book
    extra = 0  # Отключаем автоматическое добавление пустых форм для создания книг


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [BookInline]







admin.site.register(Library, LibraryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)