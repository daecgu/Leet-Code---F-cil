def arraysign(nums):
    cuenta = 1
    for each in nums:
        if each == 0:
            return 0
        else:
            if each < 0:
                cuenta = -cuenta
    return cuenta

array=[1,2,-1,5,6,-9,1]
print(arraysign(array))