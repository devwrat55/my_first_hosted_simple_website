import sys

def relacingtexts(old,new):
	with open('/var/www/html/index.html', 'r') as file :
  		filedata = file.read()
	
    	# Replace the target string
	filedata = filedata.replace(old, new)
	
	# Write the file out again
	with open('/var/www/html/index.html', 'w') as file:
	  file.write(filedata)


if __name__ == "__main__":
    	new = str(sys.argv[1])
    	old = "images"
    	relacingtexts(old, new)
