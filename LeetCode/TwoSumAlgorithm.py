class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        indecies = []
        for num in nums:
            x += num
            indecies.append(nums.index(num))
            if x % target == 0:
                return indecies
            elif x % target > 0:
                nums.pop(0)
                x = x - nums[nums.index(num)]
                continue




class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numbers = []
        # number = [[nums.index(num) for num in nums if nums[fn_counter] + num == target and fn_counter is not nums.index(num)] for fn_counter in range(len(nums))]
        for fn_counter in range(len(nums)):
        #     number = [nums.index(num) for num in nums if nums[fn_counter] + num == target and nums.index(num) != fn_counter]
        #     if number:
        #         numbers.append(number[0])
        # return numbers

            for num in nums:
                n_index = nums.index(num)
                if n_index == fn_counter:
                    continue
                elif nums[fn_counter] + num == target:
                    return [fn_counter, n_index]

test = Solution()
print(test.twoSum([3,3], 6))





