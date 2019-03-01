import click
import csv
import frontmatter
import os
import requests

from lxml.html import fromstring
from urllib.parse import urlsplit

from commands.common import CONTEXT_SETTINGS, common_params


def fetch_title(url):
    r = requests.get(url)
    tree = fromstring(r.content)
    title = tree.findtext('.//title')

    return title

def sluggify(string):
    string = string.replace(':', '')
    string = string.replace(' ', '-')
    string = string.lower()

    return string

def get_markdown_url(url):
    url_data = urlsplit(url)
    if url_data.netloc == 'hackmd.io':
        url = url + '/download'

    return url

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--resource-list',
              required=True,
              help='CSV file listing the urls to backup.',
              )
@click.option('--destination',
              required=True,
              help='Local path or GitHub repo in which to write backups. Ex: path/to/dir, someorg/myrepo',
              envvar='BACKUP_DESTINATION',
              )
@click.option('--github-token',
              help='Personal access token for GitHub API.',
              envvar="GITHUB_API_TOKEN",
              )
@common_params
def backup2github(resource_list, github_token, destination, yes, verbose, debug, noop):
    """Backup a list of URLs to a destination directory or GitHub repo.

    The format of the --resource-list is expected to be a local CSV. Columns
    are as follows:

        - do_backup. If column is present, empty rows will not be backed up.

        - resource_url. The URL to the file for backup. Supports raw files
            directly.

        - Any other columns will be ignored.

    Currently supported destination is a local directory. GitHub repos coming
    soon.

    Currently supported backup URLs:

        - any raw files

        - HackMD web urls (fetched as markdown)

    When processing markdown files, YAML frontmatter can be used for certain
    keys:

        - filename: Allows overriding of the filename, normally processed from
            header. Ex: myfile.md

        - path: Allows nesting the backup file in a subdirectory.
    """
    if debug: click.echo('>>> Debug mode: enabled')
    if noop: click.echo('>>> No-op mode: enabled (No operations affecting data will be run)')

    if debug or yes or verbose:
        raise "Provided option not yet implemented"

    if os.path.isdir(destination):
        # we are writing to a directory
        click.echo('Getting ready to write to directory...')
    else:
        # we are writing to github repo
        # check if api token provided
        # check if repo exists
        raise 'Backup to GitHub repos not yet supported.'

    # process CSV
    with open(resource_list) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # If column exists and doesn't have tick, skip.
            if not row.get('do_backup', True):
                continue

            url = row['resource_url']

            # Skip empty fields.
            if not url:
                continue

            title = fetch_title(url)
            title = title.replace(' - HackMD', '')
            title = title.replace(' Toronto Workers Co-op:', '')
            title = sluggify(title)
            filename = title + '.md'
            filepath = os.path.join(destination, filename)

            url = get_markdown_url(url)
            r = requests.get(url)
            markdown = r.content.decode('utf-8')
            post = frontmatter.loads(markdown)

            # Append source url to frontmatter.
            post.metadata['source'] = row['resource_url']
            markdown = frontmatter.dumps(post)

            metadata = post.metadata
            if metadata.get('filename'):
                filename = metadata['filename']

            if metadata.get('path'):
                filepath = os.path.join(destination, metadata['path'])
                if not noop:
                    makedirs(filepath)
            else:
                filepath = destination

            filepath = os.path.join(filepath, filename)

            # TODO: Do a safety check to ensure we're not outside destination path.
            click.echo('Writing file: ' + filepath)
            if not noop:
                with open(filepath, 'w') as f:
                    f.write(markdown)
                    f.write("\n")

            # TODO: process hackmd-specific formatting.

    if noop: click.echo('Command exited no-op mode without creating/updating any events.')
