# Binary search
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    if len(nums2) < len(nums1): nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)  
        
    left, right = 0, m-1
    while True:
        pointer1 = left + (right-left) // 2
        pointer2 = (m+n)//2 - pointer1 - 2
            
        left1 = nums1[pointer1] if pointer1 in range(m) else float("-inf")
        left2 = nums2[pointer2] if pointer2 in range(n) else float("-inf")
        right1 = nums1[pointer1+1] if pointer1+1 in range(m) else float("inf")
        right2 = nums2[pointer2+1] if pointer2+1 in range(n) else float("inf")
            
        if left1 <= right2 and left2 <= right1:
            if (m+n) % 2 == 0: return (max(left1, left2) + min(right1, right2)) / 2
            else: return min(right1, right2)
                
        elif left1 > right2: right = pointer1 - 1
        else: left = pointer1 + 1

# Merge and sort
def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1) 
    return (nums1[n//2] + nums1[(n-1)//2])/2.0