# -*- coding: utf-8 -*-
import time
import math


doneFrame = '█'
fgFrame = '▒'
bgFrame = '░'


def bar(now, all, lenght=30):
    process = now/all
    done1 = math.floor(process*lenght)
    done2 = math.ceil(process*lenght)-done1
    wait = lenght - done1 - done2
    return '{}{}{}  {:.2f}%'.format(doneFrame*done1, fgFrame*done2, bgFrame*wait, process*100)


print('\x1b[?25l', end='', sep='')
for i in range(101):
    print('\r', bar(i, 100), end='', sep='')
    time.sleep(0.05)
print('\x1b[?25h\x1b[1B', end='', sep='')
