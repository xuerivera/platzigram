from django.contrib import admin

from users.models import Profile


# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')


    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )

    readonly_fields = ('created', 'modified')


class profileInline(admin.StackedInline):
    """Profile Inline"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(admin.ModelAdmin):
    """User Admin"""
    inlines = (profileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff') 