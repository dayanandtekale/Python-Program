import threading
import time
start = time.perf_counter()

#init
#start
#running
#sleep
#waiting
#stop
#end/terminate

def thread(threadname, sleepTime = 1):
    print(f"Thread Started and will sleep for {sleepTime} second(s): ", threadname)
    time.sleep(sleepTime)
    # print(f"slept well {threadname} for {sleepTime} second(s)")
    print("slept well {} for {} second(s)".format(threadname, sleepTime))

t1 = threading.Thread(target=thread, args=["t1",1])
t2 = threading.Thread(target=thread, args=["t2",2])
t3 = threading.Thread(target=thread, args=["t3",3])
t4 = threading.Thread(target=thread, args=["t4"])
t5 = threading.Thread(target=thread, args=["t5"])
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

finish = time.perf_counter()
print("finished in " + str(finish-start) + " seconds")