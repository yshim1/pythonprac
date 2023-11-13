# pattern = "abba"
# s = "dog cat cat dog"
# wordsList = s.split()
# hm = {}
# for i in range(len(pattern)):
#     if pattern[i] not in hm.keys() and wordsList[i] not in hm.values():
#         hm[pattern[i]] = wordsList[i]
# print(hm)

# s = "the sky is blue"
# wordsList = s.split()
# print(wordsList)

# s2 = "  hello world  "
# words = s2.split()
# print(words)

def findMin(nums) -> int:
    l , r = 0, len(nums) - 1 
    # min_number = nums[0]
    # while l  <=  r :
    #     mid = (l + r ) // 2
    #     min_number = min(min_number,nums[mid])

    #     # min is in right section
    #     if nums[mid] > nums[r]:
    #         l = mid + 1
    #     # min is in left section
    #     else:
    #         r = mid - 1 
    # return min(min_number,nums[l])
    res = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        mid = (l + r)//2
        print('This is the mid point: ' + str(mid))
        res = min(res, nums[mid])
        print('This is the res: ' + str(res))
        if nums[l] <= nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return res

A = [3,1,2]
findMin(A)
