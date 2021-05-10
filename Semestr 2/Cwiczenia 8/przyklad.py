import os
import heapq
from timeit import default_timer as timer

# Sortowanie szybkie:
sort_list_1 = [4, 10, 11, 5, 73, 5, 1]
print(sort_list_1)
print("Sortowanie szybkie: ")
start = timer()
sort_list_1.sort()
end = timer()
print(sort_list_1)
print("Czas: ", end-start)

# Sortowanie Heap:
sort_list_2 = [4, 10, 11, 5, 73, 5, 1]
print(sort_list_2)
print("Heap Sort: ")
start2 = timer()
heapq.heapify(sort_list_2)
end2 = timer()
print(sort_list_2)
print("Czas: ", end2-start2)


