from threading import Timer
import time


def timeloop():
    print(f'--- ' + time.ctime() + ' ---')
    Timer(10, timeloop).start()
timeloop()
