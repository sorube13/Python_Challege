import urllib2
import re

def digits(text):
	for i in text:
		if i.isdigit():
			return True
	return False

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=1234f')
html = response.read()
index = 0
while digits(html):
	nothing = re.findall(r'\d+', html)[0]
	nothing_new = int(nothing)/2
	link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
	response = urllib2.urlopen(link)
	html = response.read()
	index += 1
	print index
	print link
print html

