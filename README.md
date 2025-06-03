# Filtered-and-sorted-record-of-people

This Python mini-project reads a JSON file containing people’s information, filters out incomplete records, sorts the valid data by country and age, generates separate JSON files for each country, and produces a summary report.

## Features

- Reads a JSON input file with people’s data.
- Filters out entries missing valid names or emails.
- Sorts the cleaned data by country (alphabetically) and age (ascending).
- Writes separate JSON files for each country, containing only valid entries.
- Generates a summary report text file showing total records, valid records kept, and counts per country.

## Example Input

The input JSON file should be a list of dictionaries, each representing a person with keys like 'name', 'email', 'age', and 'country'. 

Example:

'''json
[
  {
   "name": "John Doe",
    "email": "john@example.com",
    "age": 34,
    "country": "USA"
  },
  {
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 28,
    "country": "Canada"
  }
]'''

## How to Use

-Ensure python3 is installed.
-Place your input file (people.json) into project directory.
-When prompted enter the JSON file name (people.json).
-Enter a name for the summary report output file (summary.txt).

The script will:
  -Create one JSON file per country with valid people data (e.g., usa_people.json).
  -Generate a summary report file with record counts.

## Output

-Multiple JSON files named <country>_people.json, each containing all valid records for that country.
A summary report text file showing:
  -Total number of records in the input file.
  -Number of valid records kept.
  -Count of valid records per country.

## Skills Demonstrated

-Reading and writing JSON files with Python.
-Filtering and cleaning data using list comprehensions.
-Sorting data by multiple keys.
-Grouping data by a specific attribute (country).
-Writing summary reports to text files.
-Handling file input/output errors gracefully.
-Writing modular and reusable Python functions.

## Potential Improvements

-Add support for exporting country data as CSV files.
-Include larger data validation (email format checking).
-Allow command-line arguments for i/o files.
-Add logging instead of print statements.
-Implement unit tests for each function.

## Project Purpose

This project is part of my learning path in Python programming and data handling. It helps me practice key skills like file I/O, modular and reusable functions, data cleaning, sorting, grouping, and generating reports. The code is designed to be clear and modular to facilitate further enhancement and learning.
