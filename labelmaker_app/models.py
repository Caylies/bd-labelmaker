from django.db import models
from discord import ButtonStyle


class ButtonStyleChoices(models.IntegerChoices):
    PRIMARY = ButtonStyle.primary.value
    SECONDARY = ButtonStyle.secondary.value
    SUCCESS = ButtonStyle.success.value
    DANGER = ButtonStyle.danger.value


class Label(models.Model):
    label = models.CharField(blank=False, null=False, max_length=80)
    response = models.TextField(blank=False, null=False, max_length=2000, help_text="The text that will be displayed")
    ephemeral = models.BooleanField(null=False, default=False)
    style = models.SmallIntegerField(
        choices=ButtonStyleChoices, default=ButtonStyleChoices.SECONDARY, help_text="Button color"
    )
