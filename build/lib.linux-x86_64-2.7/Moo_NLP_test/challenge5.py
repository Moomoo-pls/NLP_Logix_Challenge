import urllib.request, urllib.error, urllib.parse
import time

url = 'https://www.wikipedia.org/'

def ripAndSave():
    '''
    Takes the contents of the html of Wikipedia
    Saves it to a local file named 'web-download.html'
    Prints out the elapsed time
    '''
    start_time = time.time()
    response = urllib.request.urlopen(url)
    webContent = response.read()

    htmlFile = open('web-download.html', 'w')
    htmlFile.write(webContent.decode("utf-8"))
    htmlFile.close
    print("%s seconds" % (time.time() - start_time))

