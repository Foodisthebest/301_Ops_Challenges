#!/bin/bash

# How to show time and date

# Running the date command from terminal and give a general output
echo `date`

# Assign variables
year=`date +%Y`
echo "We are on $year"

month=`date +%m`
echo "The month is $month"

day=`date +%d`
echo "Today is the $day"

# Putting it together
echo "Current date: $day-$month-$year"

# How to append content to a file

# The >> double carrot will append to the file; using > one carrot overrides the whole string
echo "My new string with date: $(date +%d-%m-%Y)"

