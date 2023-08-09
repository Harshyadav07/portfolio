# class key:
#     def missing_value(self, nums: list[int]) -> int:
#         n = len(nums)
#         for i in range(n):
#             newplace = nums[i] - 1
#             while 1 <= nums[i] <= n and nums[i] != nums[newplace]:
#                 nums[i], nums[newplace] = nums[newplace], nums[i]
#                 newplace = nums[i]-1

#     for i in range(n):
#         if i+1 != nums[i]:
#             return i+1
#     return n+1


# print(missing_value)

def missing_value(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        newplace = nums[i] - 1
        while 1 <= nums[i] <= n and nums[i] != nums[newplace]:
            nums[i], nums[newplace] = nums[newplace], nums[i]
            newplace = nums[i]-1

    for i in range(n):
        if i+1 != nums[i]:
            return i+1
    return n+1


print(missing_value([1, 3, 23, 2]))
