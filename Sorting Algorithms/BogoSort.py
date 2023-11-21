import time
import random


#This 'works'
def bogo(arr):
    length = len(arr)
    flag = False
    while not flag:
        flag = True
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                flag = False
        random.shuffle(arr)


def main():
    arr = []
    timeT = 0
    count = 100
    timeAvg = 0
    print('bogo sort')
    for j in range(count):
        arr = []
        for i in range(500):
            arr.append(random.randint(1,100))
        timeB = time.time_ns()/1000
        arrN = bogo(arr)
        timeA = time.time_ns()/1000
        timeT = (timeA - timeB)/1000
        timeAvg += timeT
        #print(str(timeT) + 'ms')
    timeAvg = timeAvg / count
    print(str(timeAvg) + 'ms  --- avg')

if __name__ == '__main__':
    main()