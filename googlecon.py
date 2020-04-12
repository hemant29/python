import urllib.request

f = urllib.request.urlopen("http://google.com/")

print(f.read(100).decode('utf-8'))