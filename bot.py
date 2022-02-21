import discord
from discord.ext import commands
from discord.ext.commands import when_mentioned_or
from cogs.utils.Cache import cache
import config
import traceback

description = f"I am simple ModMail Bot created by {config.owner_name} for {config.guild_name} "

initial_extensions = (
    f'cogs.{"UserCommands"}',
    f'cogs.{"CacheCommands"}',
)


class ModMail(commands.Bot):

    def __init__(self):
        allowed_mentions = discord.AllowedMentions(roles=True, users=True, replied_user=True)
        super().__init__(
            command_prefix=when_mentioned_or('m!'),
            allowed_mentions=allowed_mentions,
            case_insensitive=True,
            description=description,
            intents=discord.Intents.all(),
            owner_ids=config.owner_id,
        )
        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Failed to load {extension}.')
                traceback.print_exc()

    # add error handling here # TODO error handling
    async def on_ready(self):
        print(f'I have gone online, as {self.user.name}#{self.user.discriminator} on {config.guild_name}')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_guild_join(self, guild):
        if guild.id != config.guild_id:
            await guild.leave()

    async def invoke(self, ctx):
        if ctx.command is not None and 'setup' not in ctx.message.content and not cache.cache['Guild']['setup']:
            print('caught by setup check')
            await ctx.send('Please setup the bot first.')
            return
        await super().invoke(ctx)

    async def close(self):
        await super().close()

    def run(self):
        try:
            super().run(config.token, reconnect=True)
        except Exception as e:
            print(f'Running failed with: {e}')
            traceback.print_exc()





