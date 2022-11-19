
import numpy as np
#int array
array1= np.array([1,2,3,3,34,4,4,44,4],dtype=int)

print(array1,type(array1[2]))
#fload array
array2= np.array([1,2,3,3,34,4,4,44,4],dtype=float)
print(array2,type(array2[-1]))
#double
array3=np.array([1,2,'aaaa',3,3,34,4,4,44,4],dtype=str)

print(array3,type(array3[1]))


#2D OR ND
array3=np.array([[1,2,2,3,5],[5,6,7,8,8]],dtype=int)
print(array3)

array3=np.array([[1,2,2,3,5],[5,6,7,8,8]],dtype=int)
print(array3)
#transpone
array4=np.transpose([[1,2,2,3,5],[5,6,7,8,8]])
print(array4,array4.dtype)

print(999 in array4)
print(1 in array4)

array5=np.array([range(10),range(10)],int)
arraydemo=np.array([range(10),range(10)],int).reshape(10,2)
print(array5,array5.ndim)
array5=array5.reshape(10,2)
print(array5)
print("copying array 5 to array 6")
array6=array5
array6[:]=5
print(array6)
print(f'array 5 is also changed due to refernce {array5}')

print("TO PREVENT THIS !!!!!!!!")
array7=arraydemo.copy()
array7[:]=1
print(f"array 7 \n {array7} \n array demo \n{arraydemo}")
