#Find_remainder_of_array_multiplication

def remainder_mult(arr,n):
    mult=1
    for i in arr:
        mult*=i
    remain=mult%n
    print(remain)


arr = {100, 10, 5, 25, 35, 14}
n = 11
remainder_mult(arr, n)