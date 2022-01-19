#!/usr/bin/env python3

#import libraries
import sys
import csv

#create empty hash
hashClassifications = {}

#Read in previous classifications (e.g. from a previous dataset)
#Format requirements: tab-separated values with following columns:
#OTU_ID taxonomy	alternative classification and confidence	model_category	approx_size (ref)
for astrLine in csv.reader(open(sys.argv[1]), csv.excel_tab):
	if astrLine not in list(hashClassifications.keys()):
		hashClassifications[astrLine[1]] = astrLine[1:]

#Read in a taxonomically-annotated ASV table (tab-separated format)
#that has NOT been classified with model-relevant annotations

#Columns should be as follows:
#OTU_ID	taxonomy	sample1 sample2 ... samplen

#will output a new table with the model-relevant annotations in the same format as the input
aTaxa = list(hashClassifications.keys())
	
for astrLine in csv.reader(open(sys.argv[2]), csv.excel_tab):
	query = astrLine[1].strip()
	if query in aTaxa:
            aOut = [astrLine[0], astrLine[1]] + hashClassifications[query] + astrLine[2:]
            print('\t'.join(aOut))
		
	else:
            aOut = [astrLine[0]] + [astrLine[1], "", "", ""] + astrLine[2:]
            print('\t'.join(aOut))
