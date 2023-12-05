# SmartChart Suite (SCS) Database Setup
By default, the SmartChart Suite is presumed to use PostgreSQL for all components that require a traditional RDBS server. Other databases are supported at various parts of the stack, but PostgreSQL provides the most uniform approach. As such, all instructions and scripts are only designed for use with PostgreSQL at this time.

(Please note: The ClarityNLP portion of the stack also required MongoDB, which is not
covered as part of this document.)

WARNING: Precise instructions below will vary by environment, but the general process will be the same. Instructions are given using PSQL CLI and assuming that the user has sudo privilieges on the system.

These instructions are given generically in their simplest form, without additional consideration for security, et. al. Please follow your local IT security policies or use your judgment on how to approach each step.


## Initial Setup

Setup PostgreSQL according to the instructions for your Operating System.

## Locate the pg_hba.conf File

The first thing that you should do is note the location of the `pg_hba.conf` file being used by your postgre service. This can be done by logging in to PSQL and running a command.

1. Using the CLI, login to the postgres server as the administrative superuser user (e.g., postgres). For example, as a sudo account on a linux machine, you may use `sudo -u postgres psql`.
2. Run the command `SHOW hba_file;`.
3. This should output a path on the host machine of the `pg_hba.conf` file in use. For example `/etc/postgresql/14/main/pg_hba.conf`. Note the location of this file, as you will have to make minor edits to it later to align with user settings.

## Creating a Service Account

1. Using the CLI, login to the postgres server as the administrative user (e.g., postgres). For example, as a sudo account on a linux machine, you may use `sudo -u postgres psql`. (If you are still logged in from locating the `pg_hba.conf` file, you do not need to do this.)
2. Once logged into the CLI, create a user which will own or have access to your SmartChart Suite related databases with `CREATE USER scuser;` (or whatever you would like to name it). Note that this user does not need to be a superuser or have additional privilieges on the server, though it may configured however you like.
3. Add a password to your service user, with `ALTER USER scuser WITH PASSWORD 'password'`, replacing scuser and password as needed. (This may also be combined with the previous step through `CREATE USER scuser WITH PASSWORD 'password';`)

## Configuring the pg_hba.conf File
Now that you have your user created, you may opt to add an entry for them in the `pg_hba.conf` file to support multiple forms of login for the sake of management. This is not strictly require if you only intend to access the service user from the stack applications.Open the file identified previously using a text editor of your choice. (Ensure you have permissions to edit and save the file.)

For this, please follow the documentation provided by Postgres to configure what you would like to setup, such as socket connections for the user, the host connection with password, and so forth.

Here is a sample of what this might look like for host (e.g. localhost) connections.
```
host    all             scuser          127.0.0.1/32            scram-sha-256
```
These should never replace existing lines, only be added to the end of the file. After saving and exiting, restart the postgres service.

# Tables and Schema by SCS Component
## Creating Databases
There are 3 databases that must be created:
* claritynlp
* cqfruler
* registry

Prior to setting up the individual schemas, these can be created with ownership given to the service user with: `CREATE DATABASE name WITH OWNER scuser;`, replacing name and scuser as appopriate.

Please note that these database can technically be named anything, but should be kept separate and associated with the various components of the stack to which they serve (Clarity NLP's NLP API, CQF Ruler, and the Registry Manager/Registry Viewer API).

**TODO: Confirm no additional granular privs are required with full ownership.**

## ClarityNLP

**TODO: Insert full run command for `/scripts/clarityNLP/latest/clarity-nlp-postgres.ddl`**

## CQF Ruler

CQF Ruler will automatically build its own database so no action needs to be taken for setup.

## Registry Manager and Viewer API

**TODO: Write up instructions.**

# Postgres Cheat Sheet
`sudo -u postgres psql` - From bash shell, log in to psql as the postgres admin user (or any other).
`\c name` - Change current database.
`\dn` - List schemas.