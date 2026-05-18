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

#Chapter 2 Problems
#2-1
'''
a. runtime of insertion sort on k elements O(k^2) * number of times insertion sort is run O(n/k) = O(nk)
b. runtime of merge sort on n/k sublists contains tree of depth log base 2 n/k, at each level we are merging n elements so O(nlog(n/k))
c. if we approach O(nlogn) with the right component of O(nk + nlog(n/k)), k = 1 which is trivially just merge sort, if we approach O(nlogn) with the left component, 
k = logn, and the right component is O(nlog(n/logn)) = O(nlogn - nloglogn) = O(nlogn) so k = logn is the largest value of k that allows the algorithm to run in O(nlogn)
d. in practice, k should not be logn since insertion sort is more efficient on small lists due to lower constant factors, so k should be
a small constant where insertion sort is more efficient than merge sort depending on its implementation details, for example k = 10 or 20
'''

#2-2
'''
a. You need to prove that the loop invariant holds for initialization, maintenance, and termination.
b. Loop invariant (python implementation):
Initialization: At the first iteration j = n which is the last element, before the first iteration j = n+1, nums[n, n+1] is an empty
array where nums[n] is trivially the smallest element of an empty array, loop invariance holds
Maintenance: Assume invariance holds for some iteration j, if nums[j] < nums[j-1], they are swapped in nums making nums[j-1] the
smallest element in nums[j-1..n], and if nums[j] >= nums[j-1], nums is maintained keeping nums[j-1] as the smallest element in
nums[j-1..n] as well, loop invariance is maintained
Termination: The condition for loop termination is when j = i+1 and nums[j] is compared to nums[j-1] where the smallest of the two is
put into nums[j-1] followed by the larger of the two, this leaves nums[i] as the smallest element in nums[i..n] Hence, loop is correct
c. Loop invariant (python implementation):
Initialization: At the first iteration i = 0 which is the first element in nums, before the first iteration i = -1 where we are checking
nums[0, i-1], this is an empty array which is trivially sorted containing the 0 smallest elements, loop invariance holds
Maintenance: Assume loop invariance holds for some iteration i, since nums[i] is the smallest element in nums[i..n], nums[0..i] is
sorted, loop invariance holds
Termination: The condition for loop termination is when i = n-1, at this point nums[0..n-1] is sorted leaving nums[n] as the largest
number in nums, hence nums[0..n] is sorted. Hence, algorithm is correct 
d. Runtime analysis:
for every iteration i to n-1 another loop iterates through nums[i+1..n], with the starting iteration count when i = 0 being through 
nums[1..n] and the final iteration count when i = n-1 being 1 meaning the number of comparisons can be represented by the series: 
(n-1) + (n-2) +..+ 1, adding this series leaves n(n-1)/2, this represents a runtime of O(n^2), this is the same as insertion sort
'''

#2-3
'''
a. O(n)
b. 
def naive_polynomial_evaluation(a, x):
    result = 0
    for i in range(len(a)):
        variable = x
        for j in range(i):
            variable *= x
        result += a[i] * variable
    return result
runtime analysis: O(n^2) from nested loop, slower than horner's method
c.Loop invariant:
Initialization: before the first iteration, i = n, so p = sum_{k=0}^{-1}(A[k + i + 1] * x^k) = 0, this matches first line, loop invariance holds
Maintenance: assume invariant holds at the start of some iteration i, p = sum_{k=0}^{n-(i+1)}(A[k + i + 1] * x^k), this means p = the sum of A[i+1..n] * x^0..x^(n-(i+1)),
at next iteration, i will decrease by 1 meaning the left bound of the indexed array A will shift by 1 and the right bound of x^k will shift right by 1, loop invariance maintained
Termination: at the final iteration, i=-1 meaning p = the sum of A[0..n] * x^0..x^n, hence algorithm is correct
'''

#2-4
'''
a. (1,5), (2,5), (3,4), (3,5), (4, 5) (start index 1)
b. the array in reverse sorted order, it will have arithmetic series 1..n-1 = sum_{i=1}^{n-1}(i) = (n-1)(1+n-1)/2 = (n-1)(n)/2 number of inversions
c. it is the same, they are both O(n^2) and the number of inversions represents the number of times numbers will need to be shifted in insertion sort
d. 
nums = [4, 1, 8, 9, 6, 7]
def findInversions(nums, l, r):
    m = l + (r-l) // 2
    inversions = 0

    if r > l + 1:
        inversions += findInversions(nums, l, m)
        inversions += findInversions(nums, m, r)
    
    arr1 = []
    arr2 = []

    for i in range(l, m):
        arr1.append(nums[i])
    for j in range(m, r):
        arr2.append(nums[j])

    i=0
    j=0
    k=l

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            nums[k] = arr1[i]
            i += 1
            k += 1
        else:
            nums[k] = arr2[j]
            inversions += len(arr1) - i
            j += 1
            k += 1

    while i < len(arr1):
        nums[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        nums[k] = arr2[j]
        j += 1
        k += 1

    return inversions
        
print(findInversions(nums, 0, len(nums)))
'''

#3.1-2
'''
Runtime analysis:
O(n^2) since each iteration i over n-1 elements of the outer loop induces n-i iterations in the inner loop. f(n) < c(n^2) for some constant c, n_0
Ω(n^2) since each iteration i over n-1 elements of the outer loop induces n-i iterations in the inner loop. f(n) > c(n^2) for some constant c, n_0
Θ(n^2) since O(n^2) and Ω(n^2)
'''

#3.1-3
'''
an elements * 1-2an positions moved = an - 2a^2n^2 = Ω(n^2), 1/n < a < 1/2, a = 1/n maximizes the number of times that the n largest values must pass through each of the middle 
(1-2a)n array positions
'''