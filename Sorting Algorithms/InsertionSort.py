import time
import random


def insertion(arr):
    length = len(arr)
    for i in range(length):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j-1], arr[j]
            j -= 1


def main():
    arr = []
    timeT = 0
    count = 100
    timeAvg = 0
    print('insertion sort')
    for j in range(count):
        arr = []
        for i in range(500):
            arr.append(random.randint(1,100))
        timeB = time.time_ns()/1000
        arrN = insertion(arr)
        timeA = time.time_ns()/1000
        timeT = (timeA - timeB)/1000
        timeAvg += timeT
        #print(str(timeT) + 'ms')
    timeAvg = timeAvg / count
    print(str(timeAvg) + 'ms  --- avg')

if __name__ == '__main__':
    main()