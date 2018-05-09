#!/usr/bin/python3

def fieldslicer(connfile, verbose, fields):
	import progressbar
	fields = fields.split(",")
	connfile = open(connfile,"r").readlines()
	outputfile = open("output.txt","a+")
	if verbose == True:
		counter = 1
		for line in connfile:
			print("Processing line " + str(counter) + " out of " + str(len(connfile)))
			count = 0
			tabseperated = line.split("\t")
			for field in fields:
				field = int(field) - 1
				outputfile.write(tabseperated[field])
				count +=1
				if count < len(fields):
					outputfile.write("\t")
				elif count == len(fields):
					outputfile.write("\n")
			counter+=1
			
	elif verbose == False:
		for idx,line in enumerate(connfile):
			progressbar.progressbar(idx,len(connfile))
			count = 0
			tabseperated = line.split("\t")
			for field in fields:
				field = int(field) - 1
				outputfile.write(tabseperated[field])
				count +=1
				if count < len(fields):
					outputfile.write("\t")
				elif count == len(fields):
					outputfile.write("\n")
