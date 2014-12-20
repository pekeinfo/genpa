
import random
import sys
import urllib2
import simplejson
import cStringIO

from bisect import bisect
from PIL import Image

def main():
        animalicos = open("animalicos.txt","r")
        ad = open("ad.txt",'r')
        name =  random.choice(animalicos.readlines()).strip('\n')
	app =  random.choice(ad.readlines()).strip('\n')
	print picture(app+"%20"+name)
	print app + " " + name

def picture(name):
	greyscale = [
            " ",
            " ",
            ".,-",
            "_ivc=!/|\\~",
            "gjez2]/(YL)t[+T7Vf",
            "mdK4ZGbNDXY5P*Q",
            "W8KMA",
            "#%$"
            ]
	zonebounds=[36,72,108,144,180,216,252]
	im=Image.open(cStringIO.StringIO(urllib2.urlopen(get_jpg(name)).read()))
	im=im.resize((90, 45),Image.BILINEAR)
	im=im.convert("L") # convert to mono
	str=""
	for y in range(0,im.size[1]):
		for x in range(0,im.size[0]):
			lum=255-im.getpixel((x,y))
			row=bisect(zonebounds,lum)
			possibles=greyscale[row]
			str=str+possibles[random.randint(0,len(possibles)-1)]
		str=str+"\n"
	return str

def get_jpg(searchTerm):
	fetcher = urllib2.build_opener()
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=animals%20" + searchTerm + "&start=0&rsz=1&imgsz=medium&imgc=gray&imgtype=lineart"
	f = fetcher.open(searchUrl)
	imageUrl = simplejson.load(f)['responseData']['results'][0]['url']
	print "url: " + imageUrl
	return imageUrl

main()


