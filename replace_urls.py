import sys
def replacingtexts(old1,new1):
	try:
		f1 = open('/var/www/html/index.html', 'r')
		f2 = open('/var/www/html/index_copy.html', 'w')
		for line in f1:
			f2.write(line.replace(old1, new1))
		f1.close()
		f2.close()

		import os
		os.remove("/var/www/html/index.html")
		os.rename('/var/www/html/index_copy.html', '/var/www/html/index.html')	
	except:
		pass

if __name__ == "__main__":
    	new = str(sys.argv[1])
    	old = "images"
    	replacingtexts(old, new)
