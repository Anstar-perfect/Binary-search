def find_smallest(arr,left=None,right=None):
    if left is None and right is None:
        (left,right) =(0,len(arr)-1)
        #0,2
    if left>right:
        return left
    mid = left +(right-left)//2
    # 2
    if arr[mid] == mid:
        #3 != 2
        print(mid)
        print(left)
        print(right)
        return find_smallest(arr,mid+1,right)#2,2
    else:
        print(mid)
        print(left)
        print(right)
        return find_smallest(arr,left,mid-1) # 2,1
if __name__ == '__main__':
    arr = [0,1,3]
    print('The smallest missing value is',find_smallest(arr))


