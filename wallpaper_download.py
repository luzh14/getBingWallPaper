import os
import re
import urllib2
import sys


path = os.path.abspath(sys.argv[0])
url = 'http://www.bing.com'

def loadurl(url):
    try:
        conn = urllib2.urlopen(url, timeout=5)
        html = conn.read()
        return html
    except urllib2.URLError, e:
        return ''
    except Exception:
        print 'unkown exception in conn.read()'
        return ''


def download(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Windows; U; Windows NT 6.1; enUS; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url=url, headers=headers)
        conn = urllib2.urlopen(req, timeout=5)
        f = open(filename, 'wb')
        f.write(conn.read())
        f.close()
        return True
    except urllib2.URLError, e:
        print e.message, 'load', url, 'error'
        return False
    except Exception:
        print 'unknown exception in conn.read()'
        return ''


def save_pic(url, path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname, url)
    print 1
    filename = path + '/' + name[0]

    print filename + ': start'

    tryTime = 3

    while tryTime != 0:
        tryTime = tryTime - 1
        if os.path.exists(filename):
            print filename, 'exist, skip'
            return True
        else:
            f = open(filename, 'w+')
        if download('http://www.bing.com' + url, filename):
            f.close()
            break

    if tryTime != 0:
        print filename + ': over'
    else:
        print url + ": Failed to download"


def pic_list(picList, path):
    picurl = ''
    for picurl in picList:
        save_pic(picurl, path)


def picurl(path=path):
    if os.path.exists(path):
        print path, 'exist'
    else:
        os.makedirs(path)
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print 'load', url, 'error'
            continue
        else:
            break

    rePicList = 'g_img={url: "(.*?)"'

    picList = re.findall(rePicList, html, re.S)
    print picList
    pic_list(picList, path)

#if you want to download wallpaper directly, you can use following function and run this script.
#picurl('input path here')
