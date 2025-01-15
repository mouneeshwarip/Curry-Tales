from django.contrib import admin
from .models import About

# Register your models here.
class AboutAdmin(admin.ModelAdmin):

    list_display = (
                    'title',
                    'content',
                    'updated_on'
                    )

# Register Contact model
class ContactAdmin(admin.ModelAdmin):

    list_display = (
                    'name',
                    'email',
                    'message',
                    'read',
                    'created_on'
                )

    ordering = ('created_on',)

admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)
