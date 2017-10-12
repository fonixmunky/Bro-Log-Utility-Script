def bro(verbose, files=[]):
	import subprocess
	import os
	import time
	files = files.split("\n")
	files.pop(-1)
	
	if verbose == False:
		epoch = time.time()
		path = os.getcwd()
		os.mkdir(path + "/" + str(epoch))
		os.chdir(path + "/" + str(epoch))
		for file in files:
			subprocess.check_output(["bro","-r",file])
			newfiles = subprocess.check_output(["ls"]).split()
			for newfile in newfiles:
				combinedfile = open("combined_" + str(newfile),"a+")
				newfile = open(newfile,"r")
				combinedfile.write(newfile)
				combinedfile.close()
				newfile.close()
				
	elif verbose == True:
		count = 1
		epoch = time.time()
		path = os.getcwd()
		os.mkdir(path + "/" + str(epoch))
		os.chdir(path + "/" + str(epoch))
		print "Creating the folder " + str(epoch) + "in order to store Bro Logs safely."
		for file in files:
			print "Working on " + str(count) + " out of " + str(len(files))
			subprocess.check_output(["bro","-r",file])
			newfiles = subprocess.check_output(["ls"]).split()
			for newfile in newfiles:
				combinedfile = open("combined_" + str(newfile),"a+")
				newfile = open(newfile,"r")
				combinedfile.write(newfile)
				combinedfile.close()
				newfile.close()
			count += 1
