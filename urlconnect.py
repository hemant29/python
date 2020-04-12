#
# read the data from the URL and print it
#
import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)B