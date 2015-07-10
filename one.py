import string
import itertools
from string import maketrans


def shift(l,n):
    return list(itertools.islice(itertools.cycle(l),n,n+len(l)))

def translate(text, abc1, abc2):
	result = ""
	for t in text:
		if t in abc:
			index = abc.index(t)
			letter = abc2[index]
		else: 
			letter = t
		result+=str(letter)
	return result


abc = list(string.ascii_lowercase)
abc2 = shift(abc, 2)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

text2="http://www.pythonchallenge.com/pc/def/map.html"
# real_text = text.maketrans(abc,abc2)


real_text = translate(text,abc,abc2)
print real_text
