# fileparse.py
#
# Exercise 3.3
import csv
from pprint import pprint


def parse_csv(filename, select=None):
    #Read a CSV file into a list of records
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        records = []
        for row in rows:
            record = dict(zip(headers, row))
            records.append(record)
    return records

records = parse_csv('Data/portfolio.csv')
pprint(records)

