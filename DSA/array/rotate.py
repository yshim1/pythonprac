def rotate(arr, k):
    #Two pointer solution
    l, r = 0, len(arr) - k
    while r < len(arr) and l < k + 1:
        arr[l] = arr[l+k+1]
        arr[r] = arr[r-k]
        l += 1
        r += 1
        
    return l, r, arr

l1 = [1,2,3,4,5,6,7]
print(rotate(l1, 3))

        
    
