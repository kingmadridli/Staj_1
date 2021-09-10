from _typeshed import StrPath
import threading
import time

start = time.perf_counter()

def DoSomething():
    print("waiting one sec")
    time.sleep(1)
    print("waiting done")


t1 = threading.Thread(target=DoSomething)
t2 = threading.Thread(target=DoSomething)

t1.start()
t2.start()

finish = time.perf_counter()

print("Finished in {} sec".format(finish-start))

