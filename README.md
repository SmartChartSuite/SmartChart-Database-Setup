# Smartchart Suite Database Setup and Database Builder

**THIS REPOSITORY IS CURRENTLY A WORK IN PROGRESS, INTENDED TO REPLACE https://github.com/SmartChartSuite/Registry-Database**

For DDL based setup instructions, please see the `SETUP.md` file. For versioning, please see `VERSIONS.md`. For the list of Athena Vocabulary that is needed to build the OMOP Concept table, please see `ATHENA.md`.

# Using the Database Build Script

The Database Builder helps to manage SmartChart Suite databases, creating new schemas/tables to allow for easy expansion into new registries or environments. **Right now it is a work in progress and considered a pre-release state.**

## Known Gaps
* Has not been tested with service user accounts to ensure proper ownership of databases.
* Registry schema in SQLAlchemy builds views as tables as views are not supported out of the box. Manual running of those two SQL
scripts may be required in the short term.
* Needs additional handling for loading Athena Vocabulary and potentialy breaking down the models to speed up loading.
    * Note: Manually building the vocab schema and loading vocabulary from Athena CSVs prior to adding constraints will be much faster until this is resolved. Other schemas are not impacted by this.

## Poetry

For dependency management, the script uses Poetry for Python. Please follow installation instructions for Poetry for your OS.

Once installed, run the following commands in the root folder of this repository (where this file resides).

```
poetry install
poetry shell
```
The `poetry shell` command will load the environment with all needed dependencies.

Once in the shell, you can run the script as follows:
```
python3 src/main.py {schema} postgresql://{user}:{password}@{server}:{port}/{database}
```
For example:
```
python3 src/main.py vocab postgresql://postgres:password@localhost:5432/registry
```

Schema is a string that currently consists of the following options:
* vocab
* claritynlp

(This will be extended to allow for additional handling once the registry schemas are fully implemented, along with the viewer schema.)

The postgres connection string then follows. Pay attention the database given in the conection string, as this may vary. For example, ClarityNLP tables resides in a different database than the Registry tables generally.

Running with the "vocab" schema option will build the OMOP 5.4 tables **(WARNING: Circular Foreign Keys may not be respected)** in a "vocab" schema within the Registry database (assuming that is what you specified in the connection string).

Running with the "claritynlp" schema option will similarily build the ClarityNLP tables in an "nlp" schema within the Clarity database given.