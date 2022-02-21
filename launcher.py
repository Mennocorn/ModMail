from cogs.utils.Cache import cache
from bot import ModMail, initial_extensions
import asyncio
import traceback
import click
import config


def run_bot():
    try:
        print('this is')
        cache.load_cache()
    except Exception as e:
        click.echo(f'Starting Cache failed!')
        traceback.print_exc()
        return

    bot = ModMail()
    bot.run()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        print('this')
        # loop = asyncio.get_event_loop()
        run_bot()


if __name__ == '__main__':
    main()



