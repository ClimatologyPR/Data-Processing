import os
import numpy as np

#--- Removes spaces next to commas
def cleanFile():
	#--- Opens file as readable then copies data to y, then closes file
	data = open(wpath+filename, 'r')
	y = data.read()
	data.close()

	#--- Reopens file as writable
	data = open(wpath+filename, 'w')

	#--- test
	#print(y)

	y = y.replace(', ', ',').replace(' ,',',')

	#--- test
	#print(y)

	#--- Write data from y into file
	data.write(y)
	    
	data.close()

	print(filename+' cleaned')

#--- Opens and transposes file
def transpose():
	x = np.loadtxt(fname = wpath+filename, dtype='str', delimiter = ',')
	x = np.transpose(x)
	np.savetxt(filename, x, fmt='%s', delimiter=",")

	print(filename+' Transposed')

#--- Working path
wpath = 'C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/'
outPath = 'C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/concat/'

outputFileName = 'concatSoundings_obs_pre-1989.csv'
outputFileName1 = 'concatSoundings_obs_post-1989.csv'
outputFileNameInd = 'concatIndexes.csv'

#--- Pre-1989 Soundings Variables
header = "STATIONID,DATE,TIME,PRES,HGHT,TEMP,DWPT,RELH,MIXR,DRCT,SKNT,THTA,THTE,THTV\n"
variableTypes = "VARCHAR(4),YYYY-MM-DD,HHMMSS,hPa,m,C,C,%,g/kg,deg,knot,K,K,K\n"

#--- Post-1989 Sounding Variables
header1 = "STATIONID,DATE,TIME,PRES,HGHT,TEMP,DWPT,FRPT,RELH,RELI,MIXR,DRCT,SKNT,THTA,THTE,THTV\n"
variableTypes1 = "VARCHAR(4),YYYY-MM-DD,HHMMSS,hPa,m,C,C,C,%,%,g/kg,deg,knot,K,K,K\n"

#--- Index variables *PROBLEM: There is a vast variation of headers in index files* 
indexHeader = "Station identifier,Station number,Observation time,Station latitude,Station longitude,Station elevation,Showalter index,Lifted index,LIFT computed using virtual temperature,SWEAT index,K index,Cross totals index,Vertical totals index,Totals totals index,Convective Available Potential Energy,CAPE using virtual temperature,Convective Inhibition,CINS using virtual temperature,Equilibrum Level,Equilibrum Level using virtual temperature,Level of Free Convection,LFCT using virtual temperature,Bulk Richardson Number,Bulk Richardson Number using CAPV,Temp [K] of the Lifted Condensation Level,Pres [hPa] of the Lifted Condensation Level,Mean mixed layer potential temperature,Mean mixed layer mixing ratio,1000 hPa to 500 hPa thickness,Precipitable water [mm] for entire sounding\n"

count = 0
count1 = 0
indexCount = 0

post89 = False

directory = os.fsencode(wpath)

#with open(outPath+outputFileName, 'w') as outfile:
with open(outPath+outputFileName, 'w') as outfile, open(outPath+outputFileName1, 'w') as outfile1, open(outPath+outputFileNameInd, 'w') as indexOutfile:
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		#--- observations processing
		if filename.endswith("_obs.txt"):
			print (filename)
			with open(filename) as infile:
				for line in infile:
					#--- if line is Pre-1989 Soundings Header, writes to concatSoundings_obs_pre-1989.csv only once
					if (line == header) and count == 0:
						#print(line)
						outfile.write(line)
						count = count + 1
					#--- if line is Post-1989 Sounding Header, writes to concatSoundings_obs_post-1989.csv only once
					elif (line == header1) and count1 == 0:
						outfile1.write(line)
						count1 = count1 + 1
						post89 = True
					#--- If line is repeated header o variable type header, ignores
					elif line == header or line == variableTypes or line == header1 or line == variableTypes1:
						continue
					#--- writes line into either csv depending if file is before or after 1989 (determined by boolean value)
					else:
						#print(line)
						if post89 == False:
							outfile.write(line)
						elif post89 == True:
							outfile1.write(line)
		#--- index processing
		elif filename.endswith("_indices.txt"):
			print (filename)
			cleanFile()
			transpose()
			with open(filename) as infile:
				for line in infile:
					if line == indexHeader and indexCount == 0:
						indexOutfile.write(line)
						indexCount = indexCount + 1
					elif line == indexHeader:
						continue
					else:
						indexOutfile.write(line)
