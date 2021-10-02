# Election Analysis

## Overview of Election Audit

This project is an analysis of a recent election for the Colorado Board of Elections. The purpose of this analysis was to complete an audit of the recent congressional election. The raw data for this analysis was from a csv file provided for this analysis. The manipulation of the data and analysis was done using Python and Visual Studio Code. Some of the information that was that the election board is interested include: the total number of votes, all of the candidates in the election, the total number of votes that each candidate received, and the percentage of votes each candidate won. All of these numbers could be used to determine the winner of the election based on the popular vote. Additional information was requested about the counties involved in this election and the number of votes from each county.

## Results of Election Audit

The analysis for this project was done by creating a Python script that could read in the csv file and analyze the data. Lists and dictionaries were created to hold the vote count and the candidates. Using a for loop, the script could loop through all of the rows in the candidate_name column to get a list of candidates and tally the votes for each candidate. The winner of the election was determined by creating an if statement to check which candidate had the greatest number of votes, this was then converted into a percent. The script was adapted to find the number and names of the counties in the election as well as the total number of votes for each county and which county had the most votes. All of the results were written to a text file.

These are the results of the Colorado election audit:

- There were a total of 369,711 votes
- There were three counties in this election:
  - Jefferson
  - Denver
  - Arapahoe
- There were three candidates in this election:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The results of the number of votes and percentage for each county:
  - Jefferson County received: 10.5% of the votes with 38,855 votes.
  - Denver County received: 82.8% of the votes with 306,055 votes.
  - Arapahoe County received: 6.7% of the votes with 24,801 votes.
- The county with the largest voter turnout:
  - Denver
- The results of the number of votes and the percentage for each candidate:
  - Charles Casper Stockham received: 23.0% of the votes with 85,213 votes.
  - Diane DeGette recieved: 73.8% of the votes with 272,892 votes.
  - Raymon Anthony Doane received: 3.1% of the votes with 11,606 votes.
- The winner of the election was:
  - Diane DeGette, who recieved the majority of the vote with 73.8% and 272,892 total votes.

## Election Audit Summary

This Python script was able to determine the number and identity of the candidates and counties in this electin. Determine the total number of votes from each candidate and county. Calculate the percentage of votes that each county and candidate received and determine the winner of the election and the county with the largest turnout. This script could be adapted to get more information about this election and be translated to cover other past or future elections. Different csv files with election data could be read into this script if the data was formatted similarly. However, the script could be adapted if the data was formatted differently by changing variable names or colummn/row indices. With more data about each county this script could include information about how many people of the total population of each county voted which could be useful information for future election analysis. This script can handle larger volumes of data including more candiates and counties which could be useful other larger elections in the future.

## Resources

- Data Source: election_anaylsis.csv
- Software: Python 3.6.1, Visual Studio Code, 1.60.2

