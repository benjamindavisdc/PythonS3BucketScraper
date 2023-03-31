import urllib.request, urllib.parse, urllib.error

URL='enter presigned S3 URL here'

filehandle=urllib.request.urlopen(URL)
for line in filehandle:
    print(line.decode().strip())