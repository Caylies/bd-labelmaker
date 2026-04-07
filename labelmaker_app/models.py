from django.db import models
from discord import ButtonStyle


class ButtonStyleChoices(models.IntegerChoices):
    PRIMARY = ButtonStyle.primary
    SECONDARY = ButtonStyle.secondary
    SUCCESS = ButtonStyle.success
    DANGER = ButtonStyle.danger
    LINK = ButtonStyle.link
    PREMIUM = ButtonStyle.premium

    # Aliases
    BLURPLE = ButtonStyle.blurple
    GREY = ButtonStyle.grey
    GRAY = ButtonStyle.gray
    GREEN = ButtonStyle.green
    RED = ButtonStyle.red
    URL = ButtonStyle.url


class Label(models.Model):
    label = models.CharField(blank=False, null=False, max_length=80)
    response = models.TextField(blank=False, null=False, max_length=2000, help_text="The text that will be displayed")
    style = models.SmallIntegerField(
        choices=ButtonStyleChoices, default=ButtonStyleChoices.SECONDARY, help_text="Button color"
    )
