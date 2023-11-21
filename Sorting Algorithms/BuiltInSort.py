import time
import random

def main():
    arr = []
    timeT = 0
    count = 100
    timeAvg = 0
    print('built in sort')
    for j in range(count):
        arr = []
        for i in range(500):
            arr.append(random.randint(1,100))
        timeB = time.time_ns()/1000
        arrN = sorted(arr)
        timeA = time.time_ns()/1000
        timeT = (timeA - timeB)/1000
        timeAvg += timeT
        #print(str(timeT) + 'ms')
    timeAvg = timeAvg / count
    print(str(timeAvg) + 'ms  --- avg')

if __name__ == '__main__':
    main()