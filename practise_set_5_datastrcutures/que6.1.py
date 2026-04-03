def remove_duplicate(numbers):
    return list(set(numbers))

nums = list(map(int,input().split()))
print("orginal list",nums)
print("without repeat",remove_duplicate(nums))
