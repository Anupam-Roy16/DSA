#
# #under the root heap[i] the tree become max heap by this function
# def max_heapify(heap, size, i):
#     left_child_index = 2 * i
#     right_child_index = (2 * i) + 1
#     if left_child_index <= size and heap[left_child_index] > heap[i]:
#         largest = left_child_index
#     else:
#         largest = i
#     if right_child_index <= size and heap[right_child_index] > heap[largest]:
#         largest = right_child_index
#     if largest != i:
#         template = heap[i]
#         heap[i] = heap[largest]
#         heap[largest] = template
#
#         max_heapify(heap, size, largest)
#
#
# #under the root heap[i] the tree become min heap by this function
# def min_heapify(heap, size, i):
#     left_child_index = 2 * i
#     right_child_index = (2 * i) + 1
#     if left_child_index <= size and heap[left_child_index] < heap[i]:
#         minimum = left_child_index
#     else:
#         minimum = i
#     if right_child_index <= size and heap[right_child_index] < heap[minimum]:
#         minimum = right_child_index
#     if minimum != i:
#         template = heap[i]
#         heap[i] = heap[minimum]
#         heap[minimum] = template
#
#         min_heapify(heap, size, minimum)
#
#
# # makes a normal array to max heap array. iterate from bottom to top beyod leaf node
# def build_heap_max(heap):
#     for i in range(size // 2, 0, -1):
#         max_heapify(heap, size, i)
#
#
# # makes a normal array to min heap array. iterate from bottom to top beyod leaf node
# def build_heap_min(heap):
#     for i in range(size // 2, 0, -1):
#         min_heapify(heap, size, i)
#
# #inserts num at last of max heap aray then if this value is max then his parernt , swap iteratvely. ensures max heap always
# def insert_max_pri_queue(num):
#     global heap,size
#     heap +=[num]
#     size += 1
#     i = size
#
#     while (i//2)>0 and heap[i] > heap[i//2]:
#         heap[i],heap[i//2] = heap[i//2],heap[i]
#         i = i//2
#
# #inserts num at last of min heap aray then if this value is min then his parernt , swap iteratvely. ensures min heap always
# def insert_min_pri_queue(num):
#     global heap,size
#     heap +=[num]
#     size += 1
#     i = size
#
#     while (i//2)>0 and heap[i] < heap[i//2]:
#         heap[i],heap[i//2] = heap[i//2],heap[i]
#         i = i//2
#
#
# # extract front vslue from heap and paste last value in front and then makes the array max heap by heapify function
# def extract_max_pri_queue():
#     global heap,size
#     if size == 0:
#         print("pri_queue is empty")
#     else:
#         print(heap[1])
#         heap[1] = heap[size]
#
#         heap = heap[:size:1]
#         size -= 1
#         if size != 1:
#             max_heapify(heap,size,1)
#
# # extract front value from heap and paste last value in front and then makes the array min heap by heapify function
# def extract_min_pri_queue():
#     global heap,size
#     if size == 0:
#         print("pri_queue is empty")
#     else:
#         print(heap[1])
#         heap[1] = heap[size]
#
#         heap = heap[:size:1]
#         size -= 1
#         if size != 1:
#             min_heapify(heap,size,1)
#
# #driver for min_priority_queue
# heap = [0 , 2, 15, 20]
# size = len(heap) - 1
# build_heap_min(heap)
# extract_min_pri_queue()
# print(heap)
# extract_min_pri_queue()
# print(heap)
#
# insert_min_pri_queue(12)
# print(heap)
# insert_min_pri_queue(13)
# print(heap)
# extract_min_pri_queue()
# print(heap)
# extract_min_pri_queue()
# print(heap)
# extract_min_pri_queue()
# print(heap)
# extract_min_pri_queue()
# print(heap)
# insert_min_pri_queue(12)
# print(heap)
#
# #driver for max_priority_queue
# # heap = [0 , 2, 15, 20]
# # size = len(heap) - 1
# # build_heap_max(heap)
# # extract_max_pri_queue()
# # print(heap)
# # extract_max_pri_queue()
# # print(heap)
# #
# # insert_max_pri_queue(12)
# # print(heap)
# # insert_max_pri_queue(13)
# # print(heap)










