import pandas as pd
import sqlite3
import argparse
from typing import Tuple
import os
from csv_exceptions import CsvFileNotFound


class CsvTransform:
    pass

def validate_csv_exists(csv_filename: str) -> bool:
    return os.path.exists(csv_filename)
    
def transform(csv_filename:str, db_name:str, table_name:str) -> None:
    if not validate_csv_exists(csv_filename):
        raise CsvFileNotFound("The csv file was not found")
    df = pd.read_csv(csv_filename)
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, index=False, if_exists="replace")
    conn.close()
    print("Importing data process succeed.")

def arg_parser() -> Tuple[str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-csv", "--csv_filename", type=str, help="CSV Filename, should be on root directory")
    parser.add_argument("-db", "--db_name", type=str, help="Database name, if not passed in will be db.sqlite")
    parser.add_argument("-tn", "--table_name", type=str, help="Destination table to import CSV data")
    args = parser.parse_args()
    return args

def main() -> None:
    args = arg_parser()
    print(validate_csv_exists(args.csv_filename))
    transform(args.csv_filename, args.db_name, args.table_name)
    

if __name__ == "__main__":
    main()
