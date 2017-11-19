def bro(verbose, files=[]):
	import subprocess
	import os
	import time
	import progressbar
	files = files.split("\n")
	files.pop(-1)
	
	if verbose == False:
		epoch = time.time()
		path = os.getcwd()
		os.mkdir(path + "/" + str(epoch))
		os.chdir(path + "/" + str(epoch))
		for idx,file in enumerate(files):
			error = open("error.log",'a+')
			progressbar.progressbar(idx, len(files), "Processing " + str(len(files)) + " PCAPs")
			subprocess.call(["bro","-r",file],stderr=error)
			newfiles = subprocess.check_output(["ls"]).split()
			for newfile in newfiles:
				if "combined_" not in newfile and "error.log" not in newfile:	
					combinedfile = open("combined_" + str(newfile),"a+")
					newfile = open(newfile,"r")
					data = newfile.read()
					combinedfile.write(data)
					name = str(newfile.split()
					name = name[2].strip(",").strip("'")
					combinedfile.close()
					newfile.close()
					os.remove(path+"/"+str(epoch)+"/"+str(name))
				else:
					pass
						   
		allcombined = subprocess.check_output(["ls"]).split()
		for all in allcombined:
			count = 1
			data = open(all,"r")
			lines = data.readlines()
			data.close()
			data = open(all,"w")
			for line in lines:
				if "#" in line:
					if count==7 or count==8:
						data.write(line)
						count+=1
					else:
						count+=1
						pass
				else:
					data.write(line)
				
	elif verbose == True:
		count = 1
		epoch = time.time()
		path = os.getcwd()
		os.mkdir(path + "/" + str(epoch))
		os.chdir(path + "/" + str(epoch))
		print "Creating the folder " + str(epoch) + "in order to store Bro Logs safely."
		print "Preparing to run " +str(len(files)) + " against the Bro IDS."
		for file in files:
			print "Working on " + str(count) + " out of " + str(len(files))
			subprocess.check_output(["bro","-r",file])
			newfiles = subprocess.check_output(["ls"]).split()
			for newfile in newfiles:
				if "combined_" not in newfile:	
					combinedfile = open("combined_" + str(newfile),"a+")
					newfile = open(newfile,"r")
					data = newfile.read()
					combinedfile.write(data)
					name = str(newfile.split()
					name = name[2].strip(",").strip("'")
					combinedfile.close()
					newfile.close()
					os.remove(path+"/"+str(epoch)+"/"+str(name))
				else:
					pass
			count +=1
						   
		allcombined = subprocess.check_output(["ls"]).split()
		print "Fixing up the combined files to have only one header!"
		filecount = 1
		for all in allcombined:
			print "Working on " + str(filecount) + " out of " + str(len(allcombined))
			count = 1
			data = open(all,"r")
			lines = data.readlines()
			data.close()
			data = open(all,"w")
			for line in lines:
				if "#" in line:
					if count==7 or count==8:
						data.write(line)
						count+=1
					else:
						count+=1
						pass
				else:
					data.write(line)
			filecount+=1
