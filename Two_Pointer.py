"""Reversing a list using Two Pointer method"""

A = [1,2,3,4,5,6,7,8,9]

i = 0 
j = len(A) - 1

while (i < j) :
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

    i += 1
    j -= 1

print(f"Reversed list is {A}")


print(f"Reversed list is {', '.join(str(k) for k in A)}")
