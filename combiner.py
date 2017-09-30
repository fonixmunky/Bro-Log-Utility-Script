def combiner(verbose, outfn, fn, files=[]):
	files = files.split("\n")
	files.pop(-1)
	
	if outfn > 0:
		combined = open(outfn,"w+")
	else:
		combined = open("combined" + fn,"w+")
	if verbose == False:
		for file in files:
			temp = open(file,"r").readlines()
			for line in temp:
				if line == "#":
					pass
				else:
					combined.write(line)
		combined.close()
		
	elif verbose == True:
		count = 1
		for file in files:
			print "Combining: " + str(count) + " out of " + str(len(files))
			temp = open(file,"r").readlines()
			for line in temp:
				if line == "#":
					pass
				else:
					combined.write(line)
			count += 1
		combined.close()

