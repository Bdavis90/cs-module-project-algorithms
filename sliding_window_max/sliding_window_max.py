'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_sum = 0
    for i in range(k):
        # print(i)
        max_sum += nums[i]
        print(max_sum, 'max sum')
    
        # for start in range(1, i - k):
        #     print(start)


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_max(arr, k))

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
