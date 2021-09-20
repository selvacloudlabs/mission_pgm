"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]. 
"""

def twoSum(nums, target):
    hashmap = {}

    for idx in range(len(nums)):

        cur = nums[idx]
        # cur + x = target
        x = target - cur

        if x in hashmap : 
            return [idx,hashmap[x]]

        hashmap[cur] = idx


nums = [2,7,11,15]
target = 9

print(twoSum(nums,target))
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""
def maxProfit( prices ):
    
    min_price = float('inf')
    max_profit = 0

    for cur in prices:
        min_price = min(min_price,cur)
        profit = cur - min_price
        max_profit = max(profit,max_profit)

    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))




