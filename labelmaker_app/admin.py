from django.contrib import admin

from labelmaker_app.models import Label


# Register your models here.
@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("label", "style")
