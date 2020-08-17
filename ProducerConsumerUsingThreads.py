#Producer Consumer Code in Python By Afsana Afrin Brishty#
from threading import Thread
import time
import random
from threading import Condition
import sys

queue = []  # Common shared buffer, which is global#
queue_maxsize = 5  # My Buffer size#
full = 5
empty = 0
def empty_space(a):
    global full
    a -= 1
    print(a)
    full = a
def full_space(b):
    global empty
    b += 1
    print(b)
    empty = b
def ConsumerEmpty_space(c):
    global full
    c += 1
    # print(c)
    full = c
def ConsumerFull_space(d):
    global empty
    d -= 1
    print(d)
    empty = d

condition = Condition()


class ProducerThread(Thread):
    def run(self):
        global queue
        condition.acquire()
        if len(queue) == queue_maxsize:
            print("Queue full, producer is waiting")
            condition.wait()
            print("Space in queue, Consumer notified the producer")
        num = input("Enter your value: ")
        queue.append(num)
        print("Produced", num)
        print("Empty space:")
        empty_space(full)
        print("Full space:")
        full_space(empty)
        condition.notify()
        condition.release()
        time.sleep(3)


class ConsumerThread(Thread):
    def run(self):
        global queue
        condition.acquire()
        if not queue:
            print("Nothing in queue, consumer is waiting")
            condition.wait()
            print("Producer added something to queue and notified the consumer")
        num = queue.pop(0)
        print("Consumed", num)
        ConsumerEmpty_space(full)
        print("Full space:")
        ConsumerFull_space(empty)
        condition.release()
        time.sleep(3)


print("1.Producer \n2.Consumer \n3.Exit")
while True:
    time.sleep(5)
    choice = input("\nPlease enter your choice:")
    if choice == str("1"):
        t1 = ProducerThread()
        t1.start()
    if choice == str("2"):
        t2 = ConsumerThread()
        t2.start()
    if choice == str("3"):
        sys.exit()
