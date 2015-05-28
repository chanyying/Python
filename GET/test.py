import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("http://weibo.com/caihanyong/home?topnav=1&wvr=6")
print getImg(html)