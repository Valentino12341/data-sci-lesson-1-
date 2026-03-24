import numpy as np

list = [1,2,3,4,5,6,7,8,9,10]
the_array = np.array([1,2,3,4,5,6,7,8,9,10])
print(list,"\n\n\n")
print(the_array,"\n\n\n")

print(list*2,"\n\n\n")
print(the_array*2)








# LESSON 2
#import numpy as np


#newarray = np.array([1,2,3,4,5,6,7,8,9])
#a=newarray.reshape(3,3)

#print(a[0:2,0:2])


#zevenroster = np.arange(1,50)
#b=zevenroster.reshape(7,7)
#print(b)
#print(b[2:5,2:5])

#var10 = np.arange(1,37)

tenroster = np.arange(1,101)
a = tenroster.reshape(10,10)
print(a)

middlehokje = a[2:7, 2:7]
print(middlehokje)

eerste_rij = a[0]
print(eerste_rij)

laatste_rij = a[:,-1]
print(laatste_rij)
