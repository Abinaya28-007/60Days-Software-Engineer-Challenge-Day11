def move_zeroes(nums):
    position = 0

    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1

    return nums


# Example
nums = [0, 1, 0, 3, 12]

print("Before:", nums)
move_zeroes(nums)
print("After: ", nums)