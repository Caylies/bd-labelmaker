from typing import TYPE_CHECKING, cast

from discord import ButtonStyle, Interaction
from discord.ext import commands
from discord.ui import Button

from ballsdex.packages.countryballs import CountryBallsSpawner
from ballsdex.packages.countryballs.countryball import BallSpawnView
from labelmaker_app.models import Label

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot
    from bd_models.models import Ball


class LabelmakerCog(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    async def monkeypatch(labelmaker_cog):  # pyright: ignore[reportSelfClsParameterName]
        labels = [label async for label in Label.objects.all()]
        cog = cast("CountryBallsSpawner", labelmaker_cog.bot.get_cog("CountryBallsSpawner"))

        class BallSpawnViewOverride(BallSpawnView):
            def __init__(self, bot: "BallsDexBot", model: "Ball"):
                super().__init__(bot, model)

                for label in labels:

                    async def callback(interaction: Interaction["BallsDexBot"]):
                        await interaction.response.send_message(label.response)

                    btn = Button(label=label.label, style=cast("ButtonStyle", label.style))
                    btn.callback = callback
                    self.add_item(btn)

        cog.countryball_cls = BallSpawnViewOverride

    @commands.command()
    @commands.is_owner()
    async def labelmaker_reloadconf(self, ctx: commands.Context["BallsDexBot"]):
        await self.monkeypatch()

        await ctx.reply("Sucessfully reloaded and monkeypatched")
