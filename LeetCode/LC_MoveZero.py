arr = [1,2,3,4,5,0,3,4,50,0,0,0,7,8,0,9]

k = 0
for i in range(len(arr)):
    if arr[i] != 0 :
        arr[k] , arr[i] = arr[i] , arr[k] #swap
        k += 1
print(arr)