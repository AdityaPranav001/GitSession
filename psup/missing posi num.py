def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[correct_index], nums[i] = nums[i], nums[correct_index]
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1
if __name__ == "__main__":
    n = int(input("Enter number of elements: ").strip())
    nums = list(map(int, input("Enter space-separated numbers: ").strip().split()))
    
    print("Smallest missing positive number:", first_missing_positive(nums))
