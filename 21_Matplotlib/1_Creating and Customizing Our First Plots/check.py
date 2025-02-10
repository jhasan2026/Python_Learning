

arr = [1,2,3,4,5,6]

p = [1,1,2,3,6,2]

arr = [x-p[i] for i,x in enumerate(arr)]

print(arr)