# Workers Co-op Scripts

Helper scripts/commands for our tech workers co-op.

Many of these run automatically.

## Contents

- Scripts
  - `backup2github` command
- Technologies Used
- Local Development

## Scripts

### `backup2github` command

```
$ pipenv run python cli.py backup2github --help
Usage: cli.py backup2github [OPTIONS]

  Backup a list of URLs to a GitHub repository.

  Currently supports: HackMD.

Options:
  --resource-list TEXT  CSV file listing the urls to backup.
  --github-repo TEXT    Repo in which to create backups. Ex: someorg/myrepo
  --github-token TEXT
  -y, --yes             Skip confirmation prompts
  -v, --verbose         Show output for each action
  -d, --debug           Show full debug output
  -n, --noop            Skip API calls that change/destroy data
  -h, --help            Show this message and exit.
```

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
