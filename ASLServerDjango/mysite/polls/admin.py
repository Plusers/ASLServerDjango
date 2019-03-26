from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.forms import SelectMultiple
from .models import *
admin.site.register(Books)
admin.site.register(News)
#admin.site.register(Books_model)
# Re-register UserAdmin
class UserInline(admin.StackedInline):
    model = UserInfo
    save_model=True
    can_delete = False
    verbose_name_plural = 'Доп. информация'
# Определяем новый класс настроек для модели User
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(UserProfile)
class BookAdmin(admin.ModelAdmin):
    list_filter = (
        ('name', admin.RelatedOnlyFieldListFilter),
    )

