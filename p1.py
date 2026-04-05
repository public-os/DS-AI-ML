import numpy as np
list=[1,2,3,4,5,6,7,8,9,10]
print("5th element of list is:", list[4])
a=np.array(list)
for i in a:
    if i%2==0:
        print(list[i-1], "is even") 