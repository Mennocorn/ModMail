from discord.ext import commands
from discord.ext import tasks
from cogs.utils.Cache import cache
import asyncio
import config


class CacheFunction(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.wait_for_check.start()
        asyncio.run(self.load_channels())

    @tasks.loop(minutes=5)
    async def wait_for_check(self):
        self.check_for_save()

    def check_for_save(self):
        # if cache.initial == cache.cache:
        cache.initial = cache.cache
        cache.make_save()

    async def load_channels(self):
        if cache.cache['Guild']['setup']:
            cache.guild = self.client.get_guild(config.guild_id)
            cache.category = cache.guild.get_channel(cache.cache['Guild']['category_request'])
            cache.category_archive = cache.guild.get_channel(cache.cache['Guild']['category_archive'])

    @commands.command()
    async def save(self, ctx):
        self.check_for_save()
        await ctx.reply('Saved.', delete_after=5)
        await ctx.message.delete()


def setup(client):
    client.add_cog(CacheFunction(client))