import numpy as np

a = np.arange(9).reshape(3,3)
b = np.array([[3,2,5], [4,8,7], [7,5,6]])

print(a)
print()
print(b)

#En vertical
#Apilar las matrices tambien esta el metodo .row_stack((a,b))
print("-"*25)
c = np.vstack((a, b))
print(c)
print("-"*25)

#En horizontal tambien esta el metodo .column_stack((a,b))
d = np.hstack((a,b))
print(d)
print("-"*25)
