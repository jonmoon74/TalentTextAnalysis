#  Imports and setup
import pandas as pd
import math

# read in the excluded words list and create as a list
exclusionFile = str(input("Enter the name of the file of words to exclude: "))
excludedWordsDF = pd.read_csv(exclusionFile)
ignored_words = excludedWordsDF['WORDS'].tolist()

# read in the potential words list and create as a list
potentialFile = str(input("Enter the name of the file of words used it indictae potential: "))
potentialWordsDF = pd.read_csv(potentialFile)(potentialFile)
potential_words = potentialWordsDF['WORDS'].tolist()

# import the file to analyse
mainDF = pd.read_excel("Talent data for analysis.xlsx", sheet_name="Sheet1")

# words indicative of potential
# Excel or csv file import
# data to analyse

# Import from excel to pandas data frame

# run the analysis

# Loop by line
# Assign strengths content to variable
# Assign development areas content to variable

# Loop through strengths words,
# Count all words
# Exclude ignore words and count ignored
# Count words in indicative potential list
# Calculate percentage of potential words and return to new data frame column
# Reset counters

# Repeat for development areas words

# Calculate difference between strengths and dev areas and return to new column

# If difference positive to strengths indicate potential talent in new column, else nothing

# If potential talent indicate readiness based on difference percentage points (agree with Ruth)


def strengths_count():
    pass


def development_areas_count():
    pass


def density_calc():
    pass


# output the result to Excel
