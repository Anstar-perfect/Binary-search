def find(a,l,r,x):
    if(r>=l):
        mid = 1 + (r-l)//2

        if a[mid] == x:
            return mid
        elif a[mid]>x :
            find(a,l,mid-1,x)
        else :
            find(a,mid+1,r,x)
    else:
        return -1
a = [1,2,3,4,5]
x=4
result = find(a,0,len(a)-1,x)
if result != -1:
    print(" Element {} is found at index {}".format(x,result))
else:
    print('The element is not found in the array')    

