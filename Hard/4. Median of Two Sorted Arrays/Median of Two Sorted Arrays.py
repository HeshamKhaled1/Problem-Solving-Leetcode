class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        tot = int(m+n)
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        if (tot) % 2 != 0 :
            indix = int(tot/2)
            return_value = nums1[indix]
            return float(return_value)
        else :
            first_indix = int(tot/2)-1
            second_indix = int(tot/2)
            return_value = nums1[first_indix] + nums1[second_indix]
            return float(return_value/2)