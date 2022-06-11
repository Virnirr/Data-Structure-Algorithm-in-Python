import random

PIVOT_FIRST = False
total_count = 0

def quick_sort(alist):
   global total_count
   total_count = 0
   quick_sort_helper(alist,0,len(alist)-1)
   return total_count

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quick_sort_helper(alist,first,splitpoint-1) # split into left half of pivot index
       quick_sort_helper(alist,splitpoint+1,last)  # split into right half of pivot index

def partition(alist,first,last):
   global total_count
   piv_index = first

   if not PIVOT_FIRST: # write code for selecting pivot based on median of 3 (first/mid/last)
      check_median = []
      check_median.append(first)
      check_median.append(last)
      check_median.append((last - first) // 2)
      check_median.sort(key=lambda x : alist[x])

      # swapping median with first index value
      piv_index = check_median[1]

   pivotvalue = alist[piv_index]
   alist[piv_index] = alist[first] # move pivot out of the way
   alist[first] = pivotvalue       # by swapping with first element

   leftmark = first+1              # left index
   rightmark = last                # right index

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           total_count += 1
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           total_count += 1
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   alist[first] = alist[rightmark]      # swap pivotvalue and element at rightmark
   alist[rightmark] = pivotvalue

   return rightmark                     # return splitpoint

if __name__ == '__main__':

    n = 800

    my_randoms = random.sample(range(100000), n)
    count = quick_sort(my_randoms)
    # print ("n =", n, "Final:", my_randoms, "\n count =", count)
    print ("n =", n, "\n count =", count)
    my_list = list(range(n))
    quick_sort(my_list)
    #print ("n =", n, "Final:", my_list, "\n count =", total_count)
    print ("n =", n, "\n count =", total_count)