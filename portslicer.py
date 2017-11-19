def portslicer(connfile, verbose, ports=[]):
	import progressbar
	ports = ports.split(",")
	connfile = open(connfile,"r").readlines()
	if verbose == True: #Perform slicing loudly
		for port in ports:
			count = 1
			print "Retrieving port: " + str(port)
			portfile = open(str(port)+".txt","w+")
			portfile.write("Originating IP" + "\t" + "Originating Port" + "\t" + "Originating Bytes" + "\t" + "Responding IP" + "\t" + "Responding Port" + "\t" + "Responding Bytes" + "\t" + "Conn State" + "\n")
			for line in connfile:
				tabseperated = line.split("\t")
				if tabseperated[5] == port:
					print "Processing line " + str(count) + " out of " + str(len(connfile)) + " for port " + str(port)
					portfile.write(tabseperated[2] + "\t" + tabseperated[3] + "\t" + tabseperated[9] + "\t" + tabseperated[4] + "\t" + tabseperated[5] + "\t" + tabseperated[10] + "\t" + tabseperated[11] + "\n")
					count+=1
				else:
					print "Processing line " + str(count) + " out of " + str(len(connfile)) + " for port " + str(port)
					count+=1
					pass
				if tabseperated[3] == port:
					print "Processing line " + str(count) + " out of " + str(len(connfile)) + " for port " + str(port)
					portfile.write(tabseperated[2] + "\t" + tabseperated[3] + "\t" + tabseperated[9] + "\t" + tabseperated[4] + "\t" + tabseperated[5] + "\t" + tabseperated[10] + "\t" + tabseperated[11] + "\n")
					count+=1
				else:
					print "Processing line " + str(count) + " out of " + str(len(connfile)) + " for port " + str(port)
					count+=1
					pass

	elif verbose == False: #perform slicing quietly 
		for idx, port in enumerate(ports):
			progressbar.progressbar(idx,len(ports))
			portfile = open(str(port)+".txt","a+")
			portfile.write("Originating IP" + "\t" + "Originating Port" + "\t" + "Originating Bytes" + "\t" + "Responding IP" + "\t" + "Responding Port" + "\t" + "Responding Bytes" + "\t" + "Conn State" + "\n")
			for line in connfile:
				tabseperated = line.split("\t")
				if tabseperated[5] == port:
					portfile.write(tabseperated[2] + "\t" + tabseperated[3] + "\t" + tabseperated[9] + "\t" + tabseperated[4] + "\t" + tabseperated[5] + "\t" + tabseperated[10] + "\t" + tabseperated[11] + "\n")
				else:
					pass
				if tabseperated[3] == port:
					portfile.write(tabseperated[2] + "\t" + tabseperated[3] + "\t" + tabseperated[9] + "\t" + tabseperated[4] + "\t" + tabseperated[5] + "\t" + tabseperated[10] + "\t" + tabseperated[11] + "\n")
				else:
					pass
