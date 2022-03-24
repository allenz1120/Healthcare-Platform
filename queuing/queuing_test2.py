import threading
import time
import logging


def task1():
    for i in range(3):
        logging.debug('Starting for the ' + str(i) + 'th time')
        time.sleep(2)
        logging.debug('Exiting for the ' + str(i) + 'th time')


def task2():
    logging.debug('Starting')
    logging.debug('Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='task1', target=task1)

t = threading.Thread(name='task2', target=task2)

d.start()
t.start()

d.join()
t.join()
