def sumOddLengthSubarrays(arr):
    x = len(arr) +1
    sum=0
    #es una respuesta lenta pero válida. se puede sumar en rango... 
    def sumarelementos(sum, arr, z):
        i=0
        while i <= len(arr)-z:
            for j in range(0,z):
                sum=sum+arr[i+j]
                j+=1
            i=i+1
        return sum

    for z in range(1,x,2):
        sum = sumarelementos(sum, arr, z)

    return sum

intento = [10,11,12,13]
print(sumOddLengthSubarrays(intento))