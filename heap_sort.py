

#input a max heap output a ascending sorted list . heap array is sorted in place 
def heap_sort_max(heap,size):
    for i in range(size-1):
        temp = heap[1]
        heap[1] = heap[size]
        heap[size] = temp
        size -= 1
        max_heapify(heap,size,1)
#for min heap        
def heap_sort_min(heap,size):
    for i in range(size-1):
        temp = heap[1]
        heap[1] = heap[size]
        heap[size] = temp
        size -= 1
        min_heapify(heap,size,1)      
#when a node's left and right subtree is heap then this function's creates a max heap with respect to this node  
def max_heapify(heap,size,i):
    left_child_index = 2*i
    right_child_index = (2*i) +1
    if left_child_index <= size and heap[left_child_index] > heap[i]:
        largest = left_child_index
    else:
        largest = i
    if right_child_index <= size and heap[right_child_index] > heap[largest]:
        largest = right_child_index
    if largest != i:
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        
        max_heapify(heap,size,largest)
 
 
 #for min heap   
def min_heapify(heap,size,i):
    left_child_index = 2*i
    right_child_index = (2*i) +1
    if left_child_index <= size and heap[left_child_index] < heap[i]:
        minimum = left_child_index
    else:
        minimum = i
    if right_child_index <= size and heap[right_child_index] < heap[minimum]:
        minimum = right_child_index
    if minimum != i:
        temp = heap[i]
        heap[i] = heap[minimum]
        heap[minimum] = temp
        
        min_heapify(heap,size,minimum)

#makes a normal array to max heap array. iterate from bottom to top beyod leaf node
def build_heap_max(heap):
    for i in  range(size//2 , 0,-1):
        max_heapify(heap,size,i)

#for min heap
def build_heap_min(heap):
    for i in  range(size//2 , 0,-1):
        min_heapify(heap,size,i)    
    
    
    
heap = [0,12,11,54,21,23,1,2,3,54,67,20,7,6,10,14,13,2,15,20]
size = len(heap) -1
build_heap_min(heap)
print(heap)
heap_sort_min(heap,size)
print(heap)


# default heapq implement min heap. for max heap elemnt is multiplied -1

# import heapq
# li = [5, 7, 9, 1, 3]
# heapq.heapify(li)
# print(li)
# heapq.heappush(li, 4)
# print(list(li))
# print(heapq.heappop(li))
# print(li)
# heapq.heappush(li, 114)
# print(list(li))

