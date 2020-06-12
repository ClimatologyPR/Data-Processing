#--- https://github.com/USGS-python/dataretrieval
#--- https://stackoverflow.com/questions/16176996/keep-only-date-part-when-using-pandas-to-datetime
#--- https://stackoverflow.com/questions/50890989/pandas-changing-the-format-of-nan-values-when-saving-to-csv

#--- first import the functions for downloading data from NWIS
import dataretrieval.nwis as nwis
 
#--- specify the USGS site code for which we want data.
stationList = open("USGS - StationIDs.txt").read().splitlines()

#--- specify the USGS parameter code for which we want data.
parameterList = ['00020','00021','00025','00030','00032','00035','00036','00045','00046','00052','46516','46529','72192','72194','99772','45587','45588','45589','45590',]

# get basic info about the site
# df = nwis.get_record(sites=stationList, service='site')
# df.to_csv(r'C:\Users\Roberto\Documents\Climatología\USGS\export_dataframe_sites_info.csv', header=True)
# print(df)

df1 = nwis.get_record(stationList, service='dv', start='2019-12-01', end='2019-12-31')

#--- Use this if table data import wizard from MySQL Workbench will be used
df1.to_csv(r'C:\Users\Roberto\Documents\Climatología\USGS\export_dataframe.csv', date_format='%Y-%m-%d', header=True, na_rep='NULL')

#--- Use this one if LOAD DATA INFILE will be used in MySQL
# df1.to_csv(r'C:\Users\Roberto\Documents\Climatología\USGS\export_dataframe.csv', date_format='%Y-%m-%d', header=True, na_rep='\\N')

print(df1)