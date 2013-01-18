#!/usr/bin/env python
#coding=utf-8
import os,sys

datalines=[]
all_depends=()

def install(module):
	cmd = "sudo easy_install %s" %s module
	os.system(cmd)

def find_depend(module):
	for n in datalines:
		if n.split(":")[0] == module:
			try:
				all_depends.append(n.split(":")[1].split(','))
			except:
				print "Error format: %s" % n
		

def install_all(module):

	find_depends(module)
	for n in all_depend:
		install(n)

def get_data():
	try:
		f_data = open("depend.data")
	except:
		try:
			f_data = urlopen("")
		except:
			print "We can open any depend.data"
			os.exit(-1)

	datelines = f_data.readlines()

if __name__ == '__main__'
	if sys.argv[1] == None:
		print "%s module_name" %s sys.argv[0] 
		os.exit(-1)

	module_name = sys.argv[1]
	install_all(module_name)
