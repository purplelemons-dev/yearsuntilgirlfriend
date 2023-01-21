
from random import randint
from time import sleep
LOOPS_PER_CHR = 64
PAUSE_TIME = 0.04
LINE_SIZE = 24

def gen_random_str(x:int):
    return "".join(str(randint(0,9)) for _ in range(x))

current=0
current_str=""
print()
while len(current_str) < LINE_SIZE:
    sleep(PAUSE_TIME)
    current+=1
    next_item=current_str+gen_random_str(LINE_SIZE - len(current_str))
    if current % LOOPS_PER_CHR == 0 and current != 0:
        current_str+=next_item[LINE_SIZE-current//LOOPS_PER_CHR]

    print(next_item, end="\r")
