# given a list of number and a number k, return whether the list add up to k. 
# eg. given[10,15,3,7] and k of 17, return true since 10 +7 is 17

def has_pair_with_sum(numbers, k):
    seen_number = set()
    for num in numbers:
        complement = k - num
        if complement in seen_number:
            return True
        seen_number.add(num)
    return False