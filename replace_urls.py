import sys
def replacingtexts(old1,new1):
	try:
	    with open('/var/www/html/index.html', 'r') as file :
	  		filedata = file.read()		
		# Replace the target string
		filedata = filedata.replace(old1, new1)
		# Write the file out again
		with open('/var/www/html/index.html', 'w') as file:
		    file.write(filedata)
	except:
		try:
			with open('/var/www/html/index.html') as f:
			    newText=f.read().replace(old1, new1)
			with open('/var/www/html/index.html', "w") as f:
			    f.write(newText)
		except:
			pass

if __name__ == "__main__":
    new = str(sys.argv[1])
    old = "images"
    replacingtexts(old, new)
