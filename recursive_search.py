def binary_search(arr,l,r,x):
    if r>=l:
        mid = 1+ (r-l)//2

        if arr[mid] ==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        else:
            return binary_search(arr,mid+1,r,x)
    else:
        return -1
arr = [1,2,3,4,5]
x = 2 

result = binary_search(arr,0,len(arr)-1,x)

if result != -1:
    print(" Element {} is found at index {}".format(x,result))
else:
    print('The element is not found in the array')
        