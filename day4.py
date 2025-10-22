# Good morning! Here's your coding interview problem for today.
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1]should give 2. The input [1, 2, 0]should give 3.
# You can modify the input array in-place.

array = [3, 4, -1, 1]

def first_missing_positive(nums):
    n = len(nums)

    # step 1: place each number in the correct spot if possible
    i = 0
    while i < n:
        correct_index = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1

    # step 2: find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([7, 8, 9, 11]))
print(first_missing_positive([1, 2, 3]))
