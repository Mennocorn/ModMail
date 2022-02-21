from discord.ext import commands
from cogs.utils.View import SetupView
from cogs.utils.Cache import cache
import discord
from typing import Union


class CreateRequest(commands.Cog):
    def __init__(self, client):
        self.client = client


class AdminSetup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setup(self, ctx):
        cache.category = new_category = await ctx.guild.create_category(name='ModMail', position=0)
        await new_category.set_permissions(ctx.guild.default_role, view_channel=False)
        cache.category_archive = archive_category = await ctx.guild.create_category(name='ModMail - Archive', position=0)
        await archive_category.set_permissions(ctx.guild.default_role, view_channel=False)
        view = SetupView()
        channel = await new_category.create_text_channel(name='Introduction')
        await channel.send('Hi', view=view)
        cache.cache['Guild']['setup'] = True
        cache.cache['Guild']['category_request'] = new_category.id
        cache.cache['Guild']['category_archive'] = archive_category.id

    @commands.command()
    async def add_mod(self, ctx, role: Union[discord.Role, discord.Member]):
        cache.cache['Guild']['mods'].append(role.id)
        await cache.category.set_permissions(role, view_channel=True)


def setup(client):
    client.add_cog(AdminSetup(client))