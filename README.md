# CsvToSQLite3

This script was created to help developers import data from CSV files to SQLite database.

# Usage and installation
Clone de repo
```
git clone https://github.com/edsonibarra/CsvToSQLite3.git
cd CsvToSQLite
```
Execute the script
```
python3 transform.py -csv <YourCSVFilePath> -db <YourDatabaseName> -tn <TheTableName>
```
Once the script has finished it will create a new file in the project's root directory
```
YourDatabaseName.sqlite
```
## Options

These are the available options for the script

|                |Required                          |Description                         |
|----------------|-------------------------------|-----------------------------|
|-csv, --csv_filename|`Y`            |Path to your csv file           |
|-db, --db_name|`Y`            |Database name            |
|-tn, --table_name          |`Y`|Table name to import data|

