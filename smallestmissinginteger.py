def solution(A):
    i = 1
    while True:
        exists = i in A
        if not exists :
            return i
        i = i + 1

A = [1, 3, 6, 4, 1, 2]
print (A)
print (solution(A))

A = [1, 2, 3]
print (A)
print (solution(A))

A = [-1, -3]
print (A)
print (solution(A))
