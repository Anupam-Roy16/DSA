
n=int(input("number of the element in list: "))
print("input data")
#for i in range(n):
v=list(map(int,input().split()))


#binary search
# while True:
#     l = 0
#     r = n - 1
#     x = int(input("Wanted element: "))
#     while l<=r:
#         #m=l+(int)((r-l)/2)
#         m=(int)((l+r)/2)#both right
#         print(v[m])
#         if v[m]==x:
#             break
#         elif v[m]>x:
#             r=m-1
#         else:
#             l=m+1
#     if l<=r:
#         print(m)
#     else:
#         print("not found")
#
#


#repeated thakle lowest index dekhabe and na thkle position dejhabe
while True:
    l = 0
    r = n - 1
    x = int(input("Wanted element: "))
    t=0
    while l<=r:
        #m=l+(int)((r-l)/2)
        m=(int)((l+r)/2)#both right
        print(v[m])
        if v[m]==x:
            r=m-1 #l=m+1 ata dile highest index dekhabe
            t=m
        elif v[m]>x:
            r=m-1
        else:
            l=m+1
    if t!=0:
        print(t)
    else:
        print("not found", l)  # l tomo indexe wanted element thakbe



def recursive_binary(v,l,r):
    m=int((l+r)/2)
    if v[m]==x:
        return m
    elif v[m]>x:
        return recursive_binary(v,l,m-1)
    else:
        return recursive_binary(v,m+1,r)

v=[3,7,7,7,12,13,14,15,19,20,21]
l=0
r=len(v)-1
x=7

g=recursive_binary(v,l,r)
print(g)



