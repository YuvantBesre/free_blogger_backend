from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class AccountAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    ordering = ('id',)
    list_display = ('email','name','created', 'modified', 'is_admin','is_staff')
    search_fields = ('email','name',)
    readonly_fields=('created', 'modified',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'is_staff', 'is_admin', 'created', 'modified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password', 'password_2', 'is_staff', 'is_admin')}
        ),
    )

admin.site.register(User, AccountAdmin)
