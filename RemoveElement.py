def removeElement(nums, val):
    global k
    k = 0
    n = len(nums)
    i = 0
    last = n - 1
    while i < n:
        if last < i:
            break
        if nums[last] == val:
            last -= 1
            continue
        if nums[i] == val:
            nums[i], nums[last] = nums[last], nums[i]
            k += 1
            i += 1
            last -= 1
            continue
        else:
            i += 1
            k += 1
    return k


a = removeElement([1,2,3,4,5,6,7,8,8,9,10], 8)
print(a)