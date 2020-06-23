import r2pipe
from os import listdir
import os
import pathlib




def iterate(directory):
	testCount = 0
	for filename in os.listdir(directory):
		check(os.path.join(directory,filename))
		testCount += 1
		if (testCount == 100):
			break

def check(file):
	try:
		r = r2pipe.open(file)
		x = r.cmd("ie")
		last = x.find("entrypoints")
		number = int(x[last - 2])

		if number == 0:
			global count0
			count0 = count0 + 1
		elif number == 1:
			global count1
			count1 = count1 + 1
		elif number == 2:
			global count2
			count2 = count2 + 1
	except Exception as e:
			raise e
	



count0 = 0
count1 = 0
count2 = 0
iterate("/Users/gavinwong/Documents/dataset/v001-part5/")
print(count0)
print(count1)
print(count2)



