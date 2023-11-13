# Program to sort the array using bubble sort technique

# function to sort the array using bubble sort
def BubbleSort(nums: int) -> None:
    temp = True
    while temp:
        temp = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                temp = True


# driver
if __name__ == '__main__':
    nums = list(map(int, input("Enter the elements of array: ").split()))
    BubbleSort(nums)
    print(f"Sorted Array: {nums}")
            

'''
OUTPUT:
Enter the elements of array: 10 7 8 9 4 3 1 5 6
Sorted Array: [1, 3, 4, 5, 6, 7, 8, 9, 10]
'''
