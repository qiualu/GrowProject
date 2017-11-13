import threading
import time


def MyThread(name,sleep):
    # cur_thread = threading.currentThread().name
    cur_thread = name
    for i in range(10):
        print('%s:%s'%(cur_thread,i))
        time.sleep(sleep)

class Thread1(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)

        self.queue = queue
        self.setDaemon(True)

    def run(self):
        for i in range(10):
            n = self.queue.get()
            print('%i get %s'%(i,n))


def main():
    # for i in range(1,4):
    #     name = 'T-%s'%i
    #     sleep = i
    #     t = threading.Thread(target=MyThread,args=(name,sleep))
    #     t.start()

    for i in range(1,4):
        name = 'T-%s'%i
        sleep = i
        t = Thread1(i)
        t.start()

if __name__ == '__main__':
    main()