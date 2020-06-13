# NWS Data Processing Source Code

These source codes are used to process .out files provided by The National Weather Service of San Juan into .csv file

## Step 1: [postProcessing_tjsj.py](https://github.com/climatologia-UPRM/data-processing/blob/master/noaa/sounding/postProcesssing_tjsj.py)

Used to extract data from .out file

Will process all .out files in `Sounding\processed_soundings_1982-2018\tjsj_soundings_1982-2018` and store processed files into `Sounding\processed_soundings_1982-2018\tjsj_soundings_1982-2018\dailyData`

Will return one **"index.txt"** and one **"observation.txt"** per .out file

## Step 2: [concat.py](https://github.com/climatologia-UPRM/data-processing/blob/master/noaa/sounding/concat.py)

Will concatenate all **"observation.txt"** files into two distinct .csv depending on their headers

Will transpose and concatenate all **"index.txt"** files into one .csv *[Problem: index header varies across all index files]*

Will return two concatenated observation .csv files and one concatenated index .csv file

### Dependencies

[NumPy](https://numpy.org/)

## [transpose.py](https://github.com/climatologia-UPRM/data-processing/blob/master/noaa/sounding/transpose.py)

Will transpose chosen **"index.txt"** file

*This file's functions are integrated in concat.py*
