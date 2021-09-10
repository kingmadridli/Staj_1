import time


start = time.perf_counter()
print(start)

def DoSomething():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done Sleeping")

DoSomething()
print(start)
DoSomething()

finish = time.perf_counter()
print(finish)

print(f"finished in {finish-start} second(s) ")
