import threading
import time
from icecream import ic

def eat(q):
    time.sleep(5)
    ic(f"1 -> eating of 5 seconds {q}")
    
def sleep():
    time.sleep(3)
    ic("2 -> sleeping of 3 seconds")
    
def code():
    time.sleep(1)
    ic("3 -> coding of 1 second")
    
eat("eee")
sleep()
code()

ic("------- 1st end --------")

ic("threading - 1")
t1 = threading.Thread(target=eat, args=("hey",)) # , comma makes that args is a tuple
t1.start()

ic("threading - 2")
t2 = threading.Thread(target=sleep)
t2.start()

ic("threading - 3")
t3 = threading.Thread(target=code)
t3.start()

ic("------- 2nd end --------")

t1.join()
t2.join()
t3.join()

ic("I'll wait because of this .join")
ic("------- 3rd end --------")
