def two_sum(nums, target):
    vistos = {}

    for i , num in enumerate(nums):
        complemento = target - num

        if complemento in vistos:
            return [vistos[complemento],i]
        
        vistos[num] = i




nums = [4,5,6,7,9,10,11]
target = 21
print(two_sum(nums, target))