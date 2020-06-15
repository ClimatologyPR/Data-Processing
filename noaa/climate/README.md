# NOAA Data Processing Source Code

These source codes are used to download datasets that will be imported into the database

## [read_ghcn.py](https://github.com/climatologia-UPRM/data-processing/blob/master/noaa/climate/read_ghcn.py)

Used for reading .dly files from NOAA's GHCN-DAILY FTP: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/

Uses **"ghcnd-stations.txt"** as a fixed list of stations to read station metadata. Retrieved from: ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

*[Further modification is needed to show attribute flags]*

Returns .csv file with climate data retrived by the station

Taken from [here](https://superuser.com/questions/1303531/open-dly-file-ghcn-noaa-data-for-analysis) author: ned haughton

### Dependencies

[pandas](https://pandas.pydata.org/)
