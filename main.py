#2.1-3
nums = [2,3,5,7,9]
val = 7
def find_val(v):
    for i in range(len(nums)):
        if nums[i] == v:
            return i
    return None
print(find_val(val))
'''
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