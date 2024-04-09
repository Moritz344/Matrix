import time 
import random
from termcolor import cprint, colored

list_1 = ["1", " ", " ", "1", "0",
          " ", "1", "1", "0", "0"]

while True:
    time.sleep(0.3)
    for _ in range(4): 
        cprint(random.choice(list_1), "green", end=' ') 
    print()  