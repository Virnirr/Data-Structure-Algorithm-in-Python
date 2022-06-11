import random
import time

def selection_sort(alist):

    comp = 0

    for i in range(len(alist) - 1, 0, -1):

        j = 1
        max_index = 0
        while j <= i:

            if alist[j] > alist[max_index]:
                max_index = j
            
            comp += 1
            j += 1
            
        temp_value = alist[i]
        alist[i] = alist[max_index]
        alist[max_index] = temp_value

    return comp


def insertion_sort(alist):

    comp = 0
    for j in range(1, len(alist)):
        
        i = j

        while i > 0 and alist[i] < alist[i-1]:
            temp = alist[i]
            alist[i] = alist[i-1]
            alist[i-1] = temp
            i -= 1
            comp += 1

        if i > 0:
            comp += 1

    return comp

def main():

    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = insertion_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()

