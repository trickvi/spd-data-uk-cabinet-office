# UK Cabinet Office Spend Publishing

This repository is a dataset for a [Spend Pulishing Dashboard](https://github.com/okfn/spend-publishing-dashboard).

The `publishers.csv` and `sources.csv` files have ben scraped from
[data.gov.uk](http://data.gov.uk).

Based on this scraped data, a set of statistics as to the quality of the published
data has collected using the [SPD Admin](https://github.com/okfn/spd-admin) tool:
this statistical data is written to the `results.csv` and `runs.csv` files.

## Installation

The tooling for managing the data is written in Python. It is recommended to create a
Py2 or Py3 virtual environment (support ranges from Python 2.7 > 3.4), and the install
the required dependencies as follows:

```
pip install -r scripts/requirements.txt
```

The installation will add the `spd-admin` tool to your PATH. Check that with:

```
spd-admin --help
```

## Working with the data

### Collecting publisher data

How we scrape publishers and their data sources.

### Collecting quality results

[SPD Admin](https://github.com/okfn/spd-admin) collects statistical data on
**publishers** and their **sources** for each given Spend Publishing Dashboard
instance, assessing the quality of each published data source, and the overall
quality of output per publisher.

#### Configuring SPD Admin

SPD Admin needs a config file. This config sets basic information for running results
and deploying the data to a remote.

A typical config file looks like this:

```
# spd-admin.config
{
    "data_dir": "data",
    "result_file": "results.csv",
    "run_file": "runs.csv",
    "source_file": "sources.csv",
    "publisher_file": "publishers.csv",
    "remotes": ["origin"],
    "branch": "master",
    "goodtables_web": "http://goodtables.okfnlabs.org"
}
```

#### Running with SPD Admin

```
spd-admin /path/to/config.json run
```

This will run a [Good Tables batch process](http://goodtables.readthedocs.org/en/latest/batch.html)
on all the data sources.

#### Deploying with SPD Admin

```
spd-admin /path/to/config.json deploy
```

This will commit the current state of the data, and push it to the remote repository.

It is possibel to run the `deploy` task with the `run` task with
`spd-admin /path/to/config.json run --deploy`. 
