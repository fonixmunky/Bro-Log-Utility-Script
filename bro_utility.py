#!/usr/bin/env python

#Imports the different modules that the script uses
import argparse
import subprocess
import textwrap
import portslicer
import fieldslicer
import combiner
import bro

#Create the command-line capability
parser = argparse.ArgumentParser(prog="Bro Log Utility Script", 
				 description=textwrap.dedent('''\
				 This program will slice conn.log's based off of a given port or field.  It will also
				 combine conn.log's together in order to make slicing and analysis easier.'''),
				 formatter_class=argparse.RawTextHelpFormatter)
mandatory = parser.add_argument_group("Mandatory",description="These are mandatory.")
optional = parser.add_argument_group("Optional", description="These are optional switches.")
mandatory.add_argument("-i", "--input", help="The path to the conn.log", metavar="")
mandatory.add_argument("-p", "--ports", help="List of ports seperated by a comma", metavar="")
mandatory.add_argument("-f", "--fields", help="List of fields seperated by a comma", metavar="")
optional.add_argument("-b", "--bro", help="Takes in the file path of PCAPs and runs thems against Bro IDS", metavar="")
optional.add_argument("-v", "--verbose", help="Outputs status to screen", action="store_true")
optional.add_argument("-c", "--combine", help=textwrap.dedent('''\
												Combine all files of a specified type into one.  Specify the path to where the 
												files are located followed by the type enclosed in quotes.  This will find all 
												files with the specified type in them.  You just have to specify the base directory. 
												
												Example: If you wanted your conn.log's combined and they are in your home 
												directory in a folder titled bro, you would type:
												
													- c "/home/user/bro/ conn.log"
																										
												This will find all conn.log's within /home/user/bro/ no matter how nested.'''), 
						 nargs=2, metavar="")
optional.add_argument("-o", "--output", help="Specify the output name when combining conn.log's", metavar="")
args = parser.parse_args()

def main():
	if args.ports > 0:
		portslicer.portslicer(args.input, args.verbose, args.ports)
	elif args.fields > 0:
		fieldslicer.fieldslicer(args.input, args.verbose, args.fields)
	elif args.combine > 0:
		#runs the linux find command to find the files the user wants to combine
		temp_files = subprocess.check_output(["find",args.combine[0],"-name",args.combine[-1]])
		combiner.combiner(args.verbose, args.output, args.combine[-1].upper(),temp_files)
	elif args.bro > 0:
		#uses the linux find command to find the pcaps to run.
		temp_files = subprocess.check_output(["find",args.bro,"-name snort.log"])
		bro.bro(args.verbose, args.bro)
		

if __name__ == "__main__":
    main()


