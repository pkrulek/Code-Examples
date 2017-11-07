# -------------------------------------------------------------------------------
# Name:        uab_reserve_location_creator
#
# Author:      Paul Krulek
#              Adds a randomized subset of Locations for the Reserve Area.
#			
#
# Created:     Oct 31, 2017
# Copyright:   (c) Dematic 2017
# Licence:     Dematic
# -------------------------------------------------------------------------------

import random


if __name__ == '__main__':
	
	INPUT_FILE = 'C:\\spe\\under-armor\\wcsfe-ee\\config\\dematic\\whimporter\\under-armor\\scripts\\input_files\\Reserve\\Complete_Reserve_Topology.csv'
	OUTPUT_FILE = 'C:\\spe\\under-armor\\wcsfe-ee\\config\\dematic\\whimporter\\under-armor\\uab\\uab-reserve-topology.csv'
	COPY_NUMBER = 1500 #Number of records to include
	
	base = open(INPUT_FILE)
	out = open(OUTPUT_FILE, 'w')
	
	lines = base.readlines()
	lines.pop(0) #remove UA header
	out.write('facility,areaName,groupName,subgroupName,locationName,locationHostName') # header used for warehouse import
	random.shuffle(lines)
	
	for i, line in enumerate(lines):
		if i >= COPY_NUMBER:
			break
		locationName = line.split(',')[5]
		out.write('\n{0},{1},{2},{3},{4},{4}'.format('UA','RESERVE','RESERVEGROUP','RESERVESUBGROUP',locationName,locationName))

	base.close()
	out.close() 