from django.contrib import admin

from extra.labelmaker.labelmaker_app.models import Label


# Register your models here.
@admin.register(Label)
class LabelAdmin:
    autocomplete_fields = ("label", "style")
