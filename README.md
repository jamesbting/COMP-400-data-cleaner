# COMP 400 Data Cleaning

This program will clean, and filter the data and produce the various datasets. Ensure the config is set properly to clean and build the right datasets. This repository actually contains 2 programs, one written in Python and one written in NodeJS.

The NodeJS program serves only to clean the champions.json file obtained from here: http://ddragon.leagueoflegends.com/cdn/11.8.1/data/en_US/champion.json. This JSON contains a lot of data about champions such as descriptions and difficulty values that are not relevant for this project. It then takes the name and key of each champion and then puts it into a new cleaned-champions.json file.

The Python program cleans the original dataset, and then produces every other dataset file required by the other programs. It creates the following files:

- filtered-dataset.csv
- filtered-dataset-no-header.csv
- post-cleaning-dataset.csv
- win_rate.txt

The program can be configured to only generate certain files. It is discussed in more detail in the configuration section

## Pre-requisites

- Python 3.9.2
- node 14.15.3

This program is not validated on any other version

## Configuration

### NodeJS program

The NodeJS program has the following configuration options:

- ```ORIGINAL_FILE```: string representing the path to the champions.json file
- ```CLEANED_FILE```: string representing the path to the cleaned-champions.json file to be written

### Python Program

The Python program expects the ```headers.txt``` file to be at ```../data/headers.txt```: The Python program has the following configuration options:

- ```clean```:
  - ```enabled```: Boolean representing if you want the program to build this dataset
  - ```original```: String representing the path to the original dataset. Must be a CSV.
  - ```cleaned```: String representing the path to the cleaned dataset. Will overwrite any existing file in that location with the same name. Includes the name and file extension, file extension must be a CSV
- ```filter_champions```:
  - ```enabled```: Boolean representing if you want the program to build this dataset
  - ```champion_dictionary```: Path to the cleaned champion dictionary built by the NodeJS program. Must be a JSON file.
  - ```output```: Path to write the new cleaned dataset file. Will overwrite any existing file in that location. Includes the name and file extension, file extension must be a CSV
  - ```output-no-header```: Path to write the new cleaned dataset file without writing the headers to the file. Will overwrite any existing file in that location with the same name. Includes the name and file extension, file extension must be a CSV
  - ```desired_columns```: List of string representing the columns that are desired from the dataset
- ```win_rate```:
  - ```enabled```: Boolean representing if you want the program to build this dataset
  - ```output```: String representing the path to the output. . Will overwrite any existing file in that location with the same name. Includes the name and file extension, file extension must be a TXT

## Running the program

To run the NodeJS program, navigate to the root of the repository and type the following command into the CLI: 

```node src/champion-cleaner.js```



To run the Python program, navigate tot he root of the repository and type the following command into the CLI:

```python src/main.py```