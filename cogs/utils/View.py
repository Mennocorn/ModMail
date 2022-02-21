import discord
from cogs.utils.Cache import cache


class RequestView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Received", style=discord.ButtonStyle.blurple, emoji='📩')
    async def receive_button_callback(self, button, interaction):
        pass

    @discord.ui.button(label='Process', style=discord.ButtonStyle.blurple, emoji='✏')
    async def process_button_callback(self, button, interaction):
        pass

    @discord.ui.button(label='Dismiss', style=discord.ButtonStyle.danger, emoji='❌')
    async def dismiss_button_callback(self, button, interaction):
        pass

    @discord.ui.button(label='Finish', style=discord.ButtonStyle.green, emoji='✅')
    async def finish_button_callback(self, button, interaction):
        pass


class SetupView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Archive', style=discord.ButtonStyle.green, emoji='✅')
    async def toggle_archive_button_callback(self, button, interaction):
        if button.style is discord.ButtonStyle.green:
            button.style = discord.ButtonStyle.danger
            button.emoji = '❌'
            cache.cache['Guild']['archive'] = False
            await interaction.response.edit_message(view=self)
        else:
            button.style = discord.ButtonStyle.green
            button.emoji = '✅'
            cache.cache['Guild']['archive'] = True
            await interaction.response.edit_message(view=self)

    @discord.ui.button(label='Delete All', style=discord.ButtonStyle.blurple, emoji='👮‍♂️')
    async def add_role_button_callback(self, button, interaction):
        await cache.category.channels[0].delete()
        await cache.category.delete()
        await cache.category_archive.delete()
        cache.cache['Guild']['setup'] = False



