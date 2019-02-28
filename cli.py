import click

from commands.backup2github import backup2github
from commands.common import CONTEXT_SETTINGS


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

cli.add_command(backup2github)

if __name__ == '__main__':
    cli()
