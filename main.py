import webbrowser
import time
import urllib.request
from bs4 import BeautifulSoup

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

while True:
    time.sleep(20)
    
    wion = urllib.request.urlopen("https://www.youtube.com/channel/UC_gUM8rL-Lrg6O3adPW9K1g/videos")
    wionsoup = str(BeautifulSoup(wion.read().decode(), 'lxml'))
    latestnews = wionsoup.find("ytimg.com/vi/") + 13

    if onetimewion:
        newurl = ''
        while wionsoup[latestnews] != '/':
            newurl += wionsoup[latestnews]
            latestnews += 1
        oldurl.append(newurl)
        onetimewion = False
    else:
        newurl = ''
        while wionsoup[latestnews] != '/':
            newurl += wionsoup[latestnews]
            latestnews += 1
        if newurl not in oldurl:
            url = "http://www.youtube.com/watch?v=" + newurl
            webbrowser.open_new_tab(url)
            oldurl.append(newurl)
