import urllib2

x = 10
while x<=52:
    url = "http://learnpythonthehardway.org/book/ex%d.html" % x
    page_name = "PythonTHW_%d.html" % x
    print url + ": \t" + page_name
    x+=1
    page = urllib2.urlopen(url)
    page_content = page.read()
    with open(page_name, 'w') as fid:
        fid.write(page_content)