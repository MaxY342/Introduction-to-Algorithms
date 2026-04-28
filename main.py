import math
#2.1-2
'''
nums = [4, 1, 8, 9, 6, 7]
def descending_insertion_sort(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        j = i-1
        while j >= 0 and nums[j] < cur:
            nums[j+1] = nums[j]
            nums[j] = cur
            j -= 1
    return nums
print(descending_insertion_sort(nums))
''' 


#2.1-3
'''
nums = [2,3,5,7,9]
val = 7
def find_val(v):
    for i in range(len(nums)):
        if nums[i] == v:
            return i
    return None
print(find_val(val))

Loop invariant:
Initialization: on the first iteration i = 0, we are checking nums[i] which is the first element. The loop
invariant holds prior to the first iteration since we are checking nums[0..i-1] which is an empty array that
cannot contain v
Maintenance: Assume the invariant holds at the start of some iteration i so v is not in nums[0..i-1].
For the iteration i, if nums[i] = v, i is returned, algorithm is correct. If nums[i] ≠ v, then
v is not in nums[0..i]. The next iteration i + 1 is started knowing that v is not in nums[0..(i+1)-1],
so the invariant is maintained for each iteration
Termination: The condition for loop termination is when i >= len(nums). Since each iteration 
increases i by 1, i = len(nums) at termination by which each element in nums[0..len(nums)-1] has
been searched. If nothing has been returned yet v is not in nums[0..len(nums)-1] and NIL is returned
Hence, the algorithm is correct.
'''

#2.2-1
'O(n^3)'

#2.2-2
'''
nums = [4, 1, 8, 9, 6, 7]
def selection_sort(nums:list[int]):
    for i in range(len(nums)-1):
        lowest = nums[i]
        lowest_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < lowest:
                lowest = nums[j]
                lowest_index = j
        if lowest != nums[i]:
            temp = nums[i]
            nums[i] = nums[lowest_index]
            nums[lowest_index] = temp
selection_sort(nums)
print(nums)

Loop Invariant:
Initialization: At first iteration i = 0, and we are checking nums[i], before this iteration we are
checking nums[0..i-1] which is an empty array which is trivially sorted containing the 0 smallest elements, loop invariant holds
Maintenance: Assume invariant holds for some iteration i, if smaller numbers than nums[i] are found in nums[i+1..len(nums)-1], nums[i]
is swaped with the smallest of those numbers, leaving nums[0..i] sorted, loop invariance is preserved. If no smaller number is found 
nums[i] remains unchanged meaning nums[0..i] is already sorted, loop invariance is preserved.
Conclusion: The condition for loop termination is when i >= len(nums)-1, since i increases by 1 each step, every element in
nums[0..len(nums)-2] is sorted and the final element nums[len(nums)-1] is the only element left meaning it is the largest
Hence, the algorithm is correct
'''

#2.2-3
'''
Average case: (n-1)/2 elements
Worst case: n-1 elements
Average case: O(n)
Worst case: O(n)
'''

#2.2-4
'''
You can add a special case that if matches the input, returns a hard coded answer.
For example for a sorting algorithm, if input is already sorted return it.
'''

#2.3-2
'''
nums = [4, 1, 8, 9, 6, 7, 1, 1, 2, 8, 10, 6, 2, 8, 8, 9, 1, 7]
def merge(nums, s, m, e):
    if e - s <= 1:
        return

    mid1 = s + (m - s) // 2
    mid2 = m + (e - m) // 2

    merge(nums, s, mid1, m)
    merge(nums, m, mid2, e)

    firstHalf = nums[s:m]
    secondHalf = nums[m:e]

    i = j = 0
    k = s

    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i] < secondHalf[j]:
            nums[k] = firstHalf[i]
            i += 1
        else:
            nums[k] = secondHalf[j]
            j += 1
        k += 1

    while i < len(firstHalf):
        nums[k] = firstHalf[i]
        i += 1
        k += 1

    while j < len(secondHalf):
        nums[k] = secondHalf[j]
        j += 1
        k += 1
merge(nums, 0, len(nums)//2, len(nums))
print(nums)
'''

#2.3-5
'''
nums = [1, 2, 5, 7, 8, 9]
def binarySearch(nums, s, e, v):
    if s > e:
        return -1
    
    middle = s + ((e-s)//2)
    
    if v == nums[middle]:
        return middle
    elif v > nums[middle]:
        return binarySearch(nums, middle, e, v)
    else:
        return binarySearch(nums, s, middle, v)
print(binarySearch(nums, 0, len(nums)-1, 7))

Worst case runtime analysis:
The depth of the recursion tree is log base 2 n since we are spliting nums in half each time, the cost at each level is constant since
we are comparing v to the middle of nums.
Therefore runtime is O(logn)
'''

#2.3-7*
'''
def sumSearch(nums, x):
    merge(nums, 0, len(nums)//2, len(nums))
    for i in range(len(nums)):
        target = x-nums[i]
        foundIndex = binarySearch(nums, 0, len(nums)-1, target)
        if foundIndex != -1 and foundIndex != i:
            return True
    return False

Runtime analysis:
merge sort takes O(nlogn) time + binary search O(logn) nested in for loop O(n) takes O(nlogn) time = O(nlogn)
'''