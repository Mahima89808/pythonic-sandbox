# # Given an array nums. We define a running sum of an array as runningSum[i] = sum(num[0] ... nums[i]).
# # Return the running sum of nums.

# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         runningSum = [0]*n
#         runningSum[0] = nums[0]

#         for i in range(1, n):
#             runningSum[i] = runningSum[i-1] + nums[i]

#         return runningSum 

# if __name__ == "__main__":
#     solution = Solution()
#     user_input = input("Enter numbers separated by spaces (e.g., 1 2 3 4): ")
#     test_input = [int(x) for x in user_input.split()]
#     result = solution.runningSum(test_input)
#     print("Running Sum Result:", result)



#                                 # Or


# user_input = input("Enter numbers separated by spaces (e.g., 1 2 3 4): ")
# test_input = [int(x) for x in user_input.split()]

# n = len(test_input)
# for i in range(1, n):
#     test_input[i] += test_input[i-1]

# print("Running Sum Result:", test_input)






# # There is a biker going on a road trip. the road trip consists of n + 1 points at different altitudes.
# # The biker starts his trip on point 0 with altitude equal 0.
# # you are given an interger array gain of length n where gain[i] is the net gain in altitude between points
# # i and i+1 for all (0 <= i < n). Return the highest altitude of a point.

# class Solution:
#     def largestAltitude(self, gain: list[int]) -> int:
#         current_altitude = 0
#         max_altitude = 0
#         n = len(gain)

#         for i in range(n):
#             current_altitude += gain[i]
#             max_altitude = max(max_altitude, current_altitude)

#         return max_altitude

# if __name__ == "__main__":
#     solution = Solution()
#     user_input = input("Enter numbers separated by spaces (e.g., 1 2 3 4): ")
#     test_input = [int(x) for x in user_input.split()]

#     result = solution.largestAltitude(test_input)

#     print("The highest altitude: ",result)

