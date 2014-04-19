# TODO: recode
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)




# # blarrghhh way

# def insertsion_sort(l):
#     for i in range(len(l)-1):
#         p1 = l[i+1]
#         count = 0
#         while p1 < l[i-count] and ((i-count)>=0):
#             l[i-count+1] = l[i-count]
#             # l[i-count+1]=p1
#             count += 1
#         l[i-count+1]=p1

# l = [9,8,9,6,1]
# insertsion_sort(l)

# print l

