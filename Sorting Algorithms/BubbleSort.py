import time
import random

def bubble(arr):
    length = len(arr)
    New = False
    for i in range(length):
        New = False
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                placeholder = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = placeholder
                New = True
        if not New:
            break

    return arr

def main():
    arr = []
    timeT = 0
    count = 100
    timeAvg = 0
    print('bubble sort')
    for j in range(count):
        arr = []
        for i in range(500):
            arr.append(random.randint(1,100))
        timeB = time.time_ns()/1000
        arrN = bubble(arr)
        timeA = time.time_ns()/1000
        timeT = (timeA - timeB)/1000
        timeAvg += timeT
        #print(str(timeT) + 'ms')
    timeAvg = timeAvg / count
    print(str(timeAvg) + 'ms  --- avg')

if __name__ == '__main__':
    main()