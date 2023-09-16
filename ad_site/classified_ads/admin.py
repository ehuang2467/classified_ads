from django.contrib import admin
from .models import Ad, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class AdAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_posted')

    inlines = [CommentInline]


admin.site.register(Ad, AdAdmin)
admin.site.register(Comment)


# Register your models here.
