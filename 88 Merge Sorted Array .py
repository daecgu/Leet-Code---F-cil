def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if n == 0:
        print("we are done")
    # elif m == 0:
    #     nums1 = nums2
    #     print(nums1)
    # elif nums2[0] >= nums1[-(n+1)] and n != 0 and m != 0:
    #     nums1 = nums1[0:(m)] + nums2
    #     print(nums1)
    # else:
    #     i = 0
    #     j = 0
    #     array3 = []
    #     while i != m or j != n:
    #         if nums1[i] <= nums2[j] and i!=m :
    #             array3.append(nums1[i])
    #             i+=1
    #         elif j!=n :
    #             array3.append(nums2[j])
    #             j+=1
    #     nums1 = array3
    #     print(nums1)
    else:
        ## Es Necesariamente esta solución ya que no se puede hacer un nums1 = ...
        ## ya que genera una neuva variable, habría que modificar la funciín para que
        ## igualar a nums1[0:n+m-] = array3[0:m+n-]
        a,b, write_index = m-1, n-1, m + n - 1
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
    print(nums1)




nums1 = [0]
nums2 = [1]
m = 0
n = 1
merge(nums1,m,nums2,n)