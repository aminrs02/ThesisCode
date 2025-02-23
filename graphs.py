def twoSum(nums: list[int], target: int) -> list[int]:
    oldnums = nums.copy()
    print(oldnums)
    for num1 in nums:
        nums.remove(num1)
        for num2 in nums:
            if num1 + num2 == target:
                return [oldnums.index(num1), oldnums.index(num2)]


print(twoSum(nums=[2, 7, 11, 15], target=9))
