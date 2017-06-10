#!/usr/bin/python

# downloadXkcd.py - Downloads every single XKCD comic.
# Modified to make it multithreaded.

import requests 
import os
import bs4
import threading


path = 'xkcd'

try:
  os.makedirs(path) # store comics in ./xkcd
except OSError as exc:
  if exc.errno == 17 and os.path.isdir(path):
    pass
  else:
    raise

def downloadXkcd(start_comic, end_comic):
  url = 'http://xkcd.com' # starting url
  for url_number in range(start_comic, end_comic):
    # Download the page.
    print('Downloading page %s...' % url_number)
    res = requests.get(url + ('/%s' % url_number))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
          comicUrl = comicElem[0].get('src')
          # Download the image.
          print('Downloading image %s...' % (comicUrl))
          res = requests.get(comicUrl)
          res.raise_for_status()
        except requests.exceptions.MissingSchema:
          # skip if not an image file
          prev = soup.select('a[rel="prev"]')[0]
          url = 'http://xkcd.com' + prev.get('href')
          continue

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

# create and start the thread objects
download_threads = []
for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
  download_thread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
  download_threads.append(download_thread)
  download_thread.start()

# wait for all the threads to end
# The main thread moves on as the other threads download comics. If there's some
# you don't want to run in the main thread until all the threads have completed
# however (further processing the downloads, for example), then you can call the
# join() method in a thread to block the program until that thread has finished.
# By using a loop to iterate over all the threads in the list, the main thread
# can call join() on each of them so they block execution until they are done.
for download_thread in download_threads:
  download_thread.join()

print('Done.') # this won't print until all join() calls have returned

