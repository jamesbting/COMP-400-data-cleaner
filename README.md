# COMP-400-data-cleaner
A script to clean the data form the Riot API Scraper. This program takes in one large uncleaned dataset file, and then can generate up to 3 different datasets:

- Cleaned dataset: This dataset is nearly identical to the original, but all the duplicate matches have been removed, and outputs a csv file with all the match statistics. Each row is a match.  Most matches are 1150 columns long, however some are not due to the amount of data returned by the Riot API. 

- Filtered Champion Dataset: This dataset contains all the team combinations from the cleaned dataset. When building this dataset, the program will remove any row from the cleaned dataset that is not exactly 1150 rows long. Each row has 11 columns, where the i-th column is the champion selected by the i-th player, for 
  $$
  0 \leq i \leq 9
  $$
  The last column contains is either a 0 or 1, representing whether the blue team won the game. 1 means  a blue victory. 

- Win Rate: This dataset contains 2 numbers, the first representing the number of matches that blue team won, and the second number represents the total number of matches encountered.

## Installation

Before running the program, ensure you have the following dependencies installed. 

- Python 3.9.2

## Before running

Before running the program, ensure that the file locations are as desired. The program initially expects that the original data files and the outputs are in a sibling folder named 'data'.

Set the 'enabled' field to ```True``` in order to build the specified dataset, and ```False``` to skip it. 

## Running the program

To run the program, go to the location that the repository is located, and issue the following command:

```
python src/main.py
```

