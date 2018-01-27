import  threading
from queue import Queue
from mymodules.spider import Spider
from mymodules.domain import *
from mymodules.general import *

PROJECT_NAME='WebCrawling'
HOMEPAGE='https://bikz007.github.io/CodePortBikz/'
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=4

queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

#Create worker threads(will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):  #underscore is used when we have to do nothinf with the value
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()


#Do the next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawled_page(threading.current_thread().name,url)
        queue.task_done()


#Each queued links is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


#Check if there is any items in the queue,if so crawl them
def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links) >0 :
        print(str(len(queued_links)) + '\tlinks in the queue left')
        create_jobs()



create_workers()
crawl()
