# Workers Co-op Scripts

Helper scripts/commands for our tech workers co-op.

Many of these run automatically.

## Contents

- Scripts
  - [`backup2github` command](#backup2github-command)
  - [`gsheet2shortlinks.py`](#gsheet2shortlinkspy)
- [Technologies Used](#technologies-used)
- [Local Development](#computer-local-development)

## Scripts

### `backup2github` command

```
$ pipenv run python cli.py backup2github --help
Usage: cli.py backup2github [OPTIONS]

  Backup a list of URLs to a destination directory or GitHub repo.

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

Options:
  --resource-list TEXT  CSV file listing the urls to backup.  [required]
  --destination TEXT    Local path or GitHub repo in which to write backups.
                        Ex: path/to/dir, someorg/myrepo  [required]
  --github-token TEXT   Personal access token for GitHub API.
  -y, --yes             Skip confirmation prompts
  -v, --verbose         Show output for each action
  -d, --debug           Show full debug output
  -n, --noop            Skip API calls that change/destroy data
  -h, --help            Show this message and exit.
```

### Task: `update_shortlinks`


Updates our `link.hypha.club` Rebrandly shortlinks from a Google Spreadsheet.

Uses [`hyphacoop/spreadsheet2shortlinks`][shortlinks-cli] commandline tool.

   [shortlinks-cli]: https://github.com/hyphacoop/spreadsheet2shortlinks

:clock1030: Runs nightly at 4am ET.  
:scroll: [Run logs][logs] accessible on Circle CI.  
:hammer_and_wrench: Configured in [`.circleci/config.yml`][config]

   [logs]: https://circleci.com/gh/hyphacoop/worker-coop-scripts/tree/master

## Technologies Used

- **Python.** A programming langauge common in scripting.
- [**Click.**][click] A Python library for writing simple command-line
  tools.
- [**CircleCI.**][circleci] A script-running service that [runs scheduled
  tasks][circleci-cron] for us in the cloud.

## :computer: Local Development

These scripts are designed to run in the cloud, using code from the
`master` branch on GitHub. However, they can also be run on a local
workstation. Further, contributions should be tested locally before
pushing changes to repo, as changes to existing scripts on `master` will
then come into effect.

### Setup

We recommend using `pipenv` for isolating your Python
environment. After installing, just follow these steps.

1. Install the required packages:

    ```sh
    # Run this only first-time or after pulling git changes.
    $ pipenv install
    ```

2. Copy the configuration file:

    ```
    $ cp sample.env .env
    ```

3. Edit the file according to its comments. (Some scripts can take
   command-line args directly.)

<!-- Links -->
   [click]: http://click.pocoo.org/5/
   [circleci]: https://circleci.com/docs/2.0/about-circleci/
   [circleci-cron]: https://support.circleci.com/hc/en-us/articles/115015481128-Scheduling-jobs-cron-for-builds-
   [config]: .circleci/config.yml
