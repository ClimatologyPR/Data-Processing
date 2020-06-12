#--- https://pypi.org/project/climata/
from climata.acis import StationDataIO

# Load average temperature for sites in Upper Klamath Lake basin
sites = StationDataIO(
    basin="18010203",
    start_date="2017-01-01",
    end_date="2017-01-31",
    parameter="avgt"
)

# Display site information and time series data
for site in sites:
    print (site.name)
    for evt in site.data:
        print (evt.date, evt.avgt)