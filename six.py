import StringIO
import zipfile
import urllib2
import re

def digits(text):
	for i in text:
		if i.isdigit():
			return True
	return False

channel = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()
z = zipfile.ZipFile(StringIO.StringIO(channel))
text = z.read('90052.txt')
# import pdb
# pdb.set_trace()

index = 0
numbers = []
while digits(text):
	nothing = re.findall(r'\d+', text)[0]
	numbers.append(nothing)
	text = z.read('%s.txt' % nothing)
	index += 1
	print index
print text
print ''.join([z.getinfo('%s.txt' % n).comment for n in numbers])