# Binary Search - finds a target value in a *sorted* array 
# With each iteration half the values in the array are eliminated

lst = [x for x in range(100)]

def BinSearch(array,target_value):
    left,right = 0,len(array)-1
    
    while left<=right:
        mid=(left+right)//2
        if array[mid] == target_value:
            return mid
        elif array[mid] > target_value:
            right=mid-1
        else:
            left=mid+1
    return -1




print(BinSearch(lst, 200))