# USGS Data Processing Source Code

These source codes are used to download datasets that will be imported into the database

## [Data.py](https://github.com/climatologia-UPRM/data-processing/blob/master/usgs/data.py)

Used for downloading USGS daily historic data in place of [USGS Daily Values Web Service URL Generation Tool](https://waterservices.usgs.gov/rest/DV-Test-Tool.html)

Uses **"USGS - StationIDs.txt"** as a fixed list of stations to fetch data from

### Dependencies

[dataretrieval 0.4](https://pypi.org/project/dataretrieval/)

## [Data2.py](https://github.com/climatologia-UPRM/data-processing/blob/master/usgs/data2.py)

*Further testing is required to determine if this library fits the project's needs*

Used for downloading USGS, and possibly NOAA, daily historic data in place of [USGS Daily Values Web Service URL Generation Tool](https://waterservices.usgs.gov/rest/DV-Test-Tool.html) or [NOAA's Climate Data Online Data Tools](https://www.ncdc.noaa.gov/cdo-web/datatools)

### Dependencies

[climata 0.5.0](https://pypi.org/project/climata/)
