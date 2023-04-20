import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *
import ssl
import urllib.request

PROJECT_NAME = 'GOOGLE-SOURCE'
HOMEPAGE = 'https://opensource.google/documentation/reference'

#context = ssl.create_default_context()
#context.check_hostname = False
#context.verify_mode = ssl.CERT_NONE
#response = urllib.request.urlopen(HOMEPAGE, context=context)

#Session.verify=False
#ssl._create_default_https_context = ssl._create_unverified_context

#response = urllib.request.urlopen(HOMEPAGE, context=ssl._create_unverified_context())

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()
