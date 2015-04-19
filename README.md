# UK Cabinet Office Spend Publishing

This repository is a dataset for a [Spend Publishing Dashboard](https://github.com/okfn/spend-publishing-dashboard).

All data is in the `data/*` directory.

The data in `publishers.csv` and `sources.csv` comes from
[data.gov.uk](http://data.gov.uk).

Based on this data, a set of statistics as to the quality of the published
data has been collected using [SPD Admin](https://github.com/okfn/spd-admin), and
is written to the `results.csv` and `runs.csv` files.

## Installation

The tooling for managing the data is written in Python. It is recommended to create a
Py2 or Py3 virtual environment (support ranges from Python 2.7 > 3.4), and to install
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

There is a very simple script now that gets a set of Cabinet House data sources
from [this data.gov.uk API response](http://data.gov.uk/api/2/rest/package/financial-transactions-data-co).

```
python scripts/get_sources.py
```

This populates `sources.csv`. `publishers.csv` was manually created
as it only has a single publisher.

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

Note that `data_dir` is either an absolute path, or a path **relative to the path of the config file**.

#### Running with SPD Admin

```
spd-admin run spd-admin.json --encoding ISO-8859-2
```

This will run a [Good Tables batch process](http://goodtables.readthedocs.org/en/latest/batch.html)
on all the data sources.

A new entry will be appended to the `results.csv` file for each data source
that is processed, and a single new entry will be added to the `runs.csv`
file to identify this run.

**Important**: *the encoding argument.*

Good Tables can automatically detect encoding, but it can also be wrong.
This allows you to explicitly pass in an encoding to be used to read the
data source stream. In the case of Cabinet Office data, auto-detection
**will** fail, so be sure to explicitly pass "ISO-8859-2" as the encoding.

#### Deploying with SPD Admin

```
spd-admin deploy spd-admin.json
```

This will commit the current state of the data, and push it to the remote repository.

It is possible to run the `deploy` task with the `run` task with
`spd-admin run spd-admin.json --deploy`. 
