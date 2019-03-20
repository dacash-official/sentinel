# DACash Sentinel

An all-powerful toolset for DACash.

[![Build Status](https://travis-ci.org/dacash-official/sentinel.svg?branch=master)](https://travis-ci.org/dacash-official/sentinel)

Sentinel is an autonomous agent for persisting, processing and automating DACash governance objects and tasks, and for expanded functions in the upcoming DACash release rebased on top of Dash V13 release (Evolution).

Sentinel is implemented as a Python application that binds to a local dacashd instance on each DACash Masternode.

This guide covers installing Sentinel onto an existing Masternode in Ubuntu 16.04 / 18.04.

## Installation

### 1. Install Prerequisites

Update system packages and ensure python and virtualenv are installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv git

Make sure the local DACash daemon is running:

    $ dacash-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/dacash-official/sentinel.git && cd sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Test the Configuration

Test the config by running all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

Run Sentinel for the first time (may take up to a minute):

    $ ./venv/bin/python bin/sentinel.py

With all tests passing and crontab setup, Sentinel will stay in sync with dacashd and the installation is complete

### 4. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '/home/YOURUSERNAME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /home/YOURUSERNAME/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

If you run it as root (mot recommended), the path could be /root/sentinel.

## Configuration

An alternative (non-default) path to the `dacash.conf` file can be specified in `sentinel.conf`:

    dacash_conf=/path/to/dacash.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Contributing

Please follow the [DACash Core guidelines for contributing](https://github.com/dacash-official/dacash/blob/master/CONTRIBUTING.md).

Specifically:

* [Contributor Workflow](https://github.com/dacash-official/dacash/blob/master/CONTRIBUTING.md#contributor-workflow)

    To contribute a patch, the workflow is as follows:

    * Fork repository
    * Create topic branch
    * Commit patches

    In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.

    Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

### License

Released under the MIT license, under the same terms as DACash Core itself. See [LICENSE](LICENSE) for more info.
