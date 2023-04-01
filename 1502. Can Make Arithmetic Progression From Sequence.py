def canMakeArithmeticProgression(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    """arr.sort()
    d = arr[1]-arr[0]
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] != d:
            return False
    return True"""

    arr.sort()
    j = arr[0]
    d = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] != j + (i) * d:
            return False
    return True