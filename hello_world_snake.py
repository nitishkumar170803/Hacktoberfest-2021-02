import time
import random

# This Code Types 'Hello World!' snake for infinite time.

interval = 0.034

while True:
    num = random.randint(3, 56)
    for i in range(num):
        print(" "*i + "Hello World!")
        time.sleep(interval)
    for i in range(num):
        print(" "*(num-i) + "Hello World!")
        time.sleep(interval)
