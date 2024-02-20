def merge( nums1 , m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index1 = 0
    index2 = 0
    while index1 < n and index2 < m:
        if nums1[index1] >= nums2[index2]:
            nums1.insert(index1, nums2[index2])
            index1 += 1
            index2 += 1
        else:
            index1 += 1
    while nums1[index1 -1] == 0:
            nums1.pop()
            index1 -= 1
    nums1 = nums1 + nums2[index2:]
    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))