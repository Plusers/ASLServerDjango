from django.contrib import admin

from .models import Books
admin.site.register(Books)

class BookAdmin(admin.ModelAdmin):
    list_filter = (
        ('name', admin.RelatedOnlyFieldListFilter),
    )

