import random
class sort:
    def __init__(self,array):
        self.array = array

    #side by side comparison and swap ascendingly and go forward as .  T.c = o(n*n)  o(n)== when already sorted
    def buble_sort(self):
        array = self.array
        i = 0
        length = len(array)
        while i < length-1:
            flag = 0
            for j in range(length-1-i):
                if array[j] > array[j+1]:
                    flag += 1
                    array[j+1],array[j] = array[j],array[j+1]
            if flag==0:
                break
            i+=1
        print(array)

    #find minimum and swap left value . left sorted right unsorted
    def selection_sort(self):
        i = 0
        array = self.array
        length = len( array )
        while(i < length-1):
            min = i
            for j in range(i+1,length):
                if array[j] < array[min]:
                    min = j
            array[min] , array[i] = array[i], array[min]
            i+=1
        print(array)


    #left is sorted and right unsorted. those value in left(sorted ) who are smaller then right val(unsorted) in loop  are gone 1 room right and then right val is paste his position
    def insertion_sort(self):
        self.array = array
        length = len(array)
        for i in range(1, length):
            hole = i - 1
            val = array[i]
            while array[hole] > val and hole >= 0:
                array[hole + 1] = array[hole]
                hole = hole - 1
            array[hole + 1] = val
        print(array)

    def merge(self,left_index,mid,right_index):
        left_array = []
        right_array = []
        array = self.array

        left_array += array[left_index : mid+1 : 1]
        right_array += array[mid+1 : right_index+1]
        i,j,k = 0,0,left_index

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                k,i = k+1,i+1
            else:
                array[k] = right_array[j]
                k, j = k + 1, j + 1

        while i < len(left_array):
            array[k] = left_array[i]
            k, i = k + 1, i + 1

        while j<len(right_array):
            array[k] = right_array[j]
            k, j = k + 1, j + 1



    def merge_sort(self,left_index,right_index):
        if left_index < right_index:
            mid = (int)((left_index+right_index)/2)
            self.merge_sort(left_index,mid)
            self.merge_sort(mid+1,right_index)
            self.merge(left_index,mid,right_index)
        else:
            return
    def print_merge_sort(self):
        print(self.array)


    def randomized_partition(self,start,end):
        'handle worst case(when all data sorted or data are same , as a result all data is one sided over pivot . t.c o(nlogn)'
        array = self.array
        piv_ind = random.randint(start,end)
        array[piv_ind] , array[end] = array[end] , array[piv_ind]
        pivot = array[end]
        tmp = start
        for i in range(start,end):
            if array[i] <= pivot:
                array[i],array[tmp] = array[tmp],array[i]
                tmp = tmp + 1
        array[tmp] , array[end]= array[end], array[tmp]
        return tmp

    def partition_last_element_pivot(self,start,end):
        array = self.array

        pivot = array[start]
        tmp = start
        for i in range(start, end):
            if array[i] <= pivot:
                array[i], array[tmp] = array[tmp], array[i]
                tmp = tmp + 1
        array[tmp],array[end] = array[end], array[tmp]
        return tmp

    def partition_first_element_pivot(self,start,end):
        array = self.array
        pivot = array[start]
        tmp = end
        for i in range(end,start,-1):
            if array[i] >= pivot:
                array[i], array[tmp] = array[tmp], array[i]
                tmp = tmp - 1
        array[tmp],array[start] = array[start], array[tmp]
        return tmp



    def quick_sort(self,start,end):
        'chaose a pivot . number less then pivot move left from pivot and number greater then pivot move right from pivot . recusively move'
        if start < end:
            pivot_index = self.partition_first_element_pivot(start,end)
            self.quick_sort(start,pivot_index - 1)
            self.quick_sort(pivot_index + 1,end)
        else:
            return
    def print_quick_sort(self):
        print(self.array)


    def counting_sort(self):
        array = self.array
        max_element = max(array)
        count_array = [0]*(max_element + 1)
        output_array = [0]*(len(array))
        for num in array:
            count_array[num] += 1

        for i in range(1,len(count_array)):
            count_array[i] += count_array[i-1]
        for num in array[::-1]:
            output_array[count_array[num] - 1] = num
            count_array[num] -= 1
        return output_array

array=[12,2,34,23,4,4,54,6,1,12,21,10]
object = sort(array)
# object.buble_sort()
# object.selection_sort()
# object.insertion_sort()
# object.merge_sort(0,len(array)-1)
# object.print_merge_sort()
print(object.counting_sort())
object.quick_sort(0,len(array)-1)
object.print_quick_sort()
print(object.quick_sort.__doc__)

