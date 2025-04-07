def jumper(nums):
    max_position = 0
    for position in range(len(nums)):
        if max_position < position:
            return False

        max_position=max(max_position, position+nums[position])
        if max_position > len(nums) - 2:
            return True


print(jumper([2,3,1,1,4])) #T
print(jumper([3,2,1,0,4])) #F

print(jumper([0, 1, 2, 3])) #F
print(jumper([0])) #T
print(jumper([1, 0, 0])) #F
print(jumper([2, 0, 0])) #T
print(jumper([1, 2, 3, 4, 5])) #T