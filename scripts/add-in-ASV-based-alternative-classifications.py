#!/usr/bin/env python3

#import libraries
import sys
import csv

#create empty hash
hashClassifications = {}

#Read in previous ASV-based classifications (e.g. from comparison to ProPortal genomes)
#Format requirements: tab-separated values with following columns (no headers):
#OTU_ID 	classification
for astrLine in csv.reader(open(sys.argv[1]), csv.excel_tab):
    hashClassifications[astrLine[0]] = astrLine[1]

#Read in a taxonomically-annotated ASV table (tab-separated format)
#that has NOT been classified with model-relevant annotations

#Columns should be as follows:
#OTU_ID	taxonomy	sample1 sample2 ... samplen

#will output a new table with the model-relevant annotations in the same format as the input
aTaxa = list(hashClassifications.keys())
	
for astrLine in csv.reader(open(sys.argv[2]), csv.excel_tab):
    query = astrLine[0].strip()
    #if ASV id matches
    if query in aTaxa:
        #print replace the 3rd column with the associated classification
        aOut = [astrLine[0], astrLine[1], hashClassifications[query]] + astrLine[3:]
        print('\t'.join(aOut))
    #do nothing if it's the first line
    elif astrLine[1] == "taxonomy":
        print('\t'.join(astrLine[0:]))
    #or if the ASV id doesn't match the dictionary
    else:
        print('\t'.join(astrLine[0:]))
