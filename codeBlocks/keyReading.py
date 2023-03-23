import simplejson as js

fileReading = open( './access.json' , 'rb' )
credentials = js.load(fileReading)
fileReading.close()

key = credentials.get('key')