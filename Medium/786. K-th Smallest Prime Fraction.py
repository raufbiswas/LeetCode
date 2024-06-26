# 786. K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while True:
            mid = (left + right) / 2
            i, count = -1, 0
            x, y = 0, 1
            
            for j in range(1, n):
                while arr[i + 1] / arr[j] < mid:
                    i += 1
                    if arr[i] * y > arr[j] * x:
                        x, y = arr[i], arr[j]
                count += i + 1

            if count == k:
                return [x, y]
            
            if count < k:
                left = mid
            else:
                right = mid