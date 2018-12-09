from django.contrib import admin

from .models import Books, User
admin.site.register(Books)
admin.site.register(User)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        ('name', admin.RelatedOnlyFieldListFilter),
    )

