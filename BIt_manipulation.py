def find_num_of_set_bit1(num):
    'bitwise and with 1 and chek value ,then right shift and repeate until n becomes 0  '
    num_of_set_bit = 0
    while num:
        if num & 1:
            num_of_set_bit += 1
        num = num >> 1
    print("num_of_set_bit: ",num_of_set_bit)


def find_num_of_set_bit2(num):
    'bitwise and with 1 and chek value ,then right shift and repeate until n becomes 0  '
    num_of_set_bit = 0
    while num:
        if num & 1:
            num_of_set_bit += 1
        num = num >> 1
    print("num_of_set_bit: ",num_of_set_bit)

def check_odd_even(num):
    'last bit of even is zero and odd is one '
    for i in range(num):
        if i & 1 == 1:
            print(i, "--- odd" )
        elif i & 1 == 0:
            print(i,"--- even")

def  extract_bit(num,index,num1):
    'num== number , from index (0th index form left), num1== number of bit for extraction from index '
    num  >>= index
    temp_num = (1<<num1)-1
    print("after extraction the number is : ",num & temp_num)

def isPowerOfTwo(x):
    # x will check if x == 0 and !(x & (x - 1)) will check if x is a power of 2 or not
    return (x and  not(x & (x - 1)))

def print_subset(array):
    'it can be also combination , hackerearth tutoreil'
    length = len(array)
    num_of_subset =  1 << length
    for i in range(num_of_subset):
        print("{",end="")
        for j in range(length):
            if (i & (1<<j)):
                print(array[j],end=",")
        print("}","\n")
# 3 2biter jonno . jodi msb 0 tahle + . jodi msb -1 tahle -. if negative num  then all bit flip and +1(2's complement)
# def absolute_val(n):
#     # include <stdio.h>
#
#     int
#     main()
#     {
#
#         int
#     n;
#     scanf("%d", & n);
#
#     int
#     nm = n >> 31;
#
#     if (nm == -1)
#     {
#     printf("sf");
#     n = n ^ 4294967295;#ones complement .  32 ta 1 paoar arecta upai hlo  (1<<31) | (1<<31)-1
#     n += 1;
#     }
#     printf("%d", n);
#
#     return 0;
#     }


if __name__=="__main__":
    find_num_of_set_bit1(7)
    check_odd_even(203)
    extract_bit(1401,2,7)
    print_subset([1,2,3,4,5])