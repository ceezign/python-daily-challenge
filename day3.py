# given an array of integers, return a new array such that each element at
# index i of new array is the product of all the number in the original array
# except the one i

def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [0] * n

    # Build the prefix products
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Build suffix products
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # multiply prefix and suffix
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result[i]

print(product_except_self([1,2,3,4,5]))

def product_except_self(nums):
    n = len(nums)
    result = [1] * n  # Step 1: start with all 1's

    # Step 2: Multiply with prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i] # update prefix product

    # Step 3: Multiply with suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i] # update suffix product
    return result

print(product_except_self([1, 2, 3, 4, 5]))
