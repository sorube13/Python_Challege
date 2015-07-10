import urllib2
import Image
import StringIO

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
html = response.read()

im = Image.open(StringIO.StringIO(html))

w,h = im.size
h2 = int(h)/2
result = ""
for i in range(0,w,7):
	pixel = im.getpixel((i,h2))
	result+= str(chr(pixel[0]))
print result

result2 = ""
for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
	result2+= str(chr(i))
print result2