import numpy as np                #    pandas ,matplotlib

# numpy = numerical python 
thelist = [5,8,18,25,36,45,75]
print(type(thelist))

thearr = np.array(thelist)
print(type(thearr))

myvar = np.array([1,4,6,8,12,15,17])
print(type(myvar))
myvar = myvar + 1000
print(myvar)
myvar= myvar - 200
print(myvar)
myvar= myvar * 200
print(myvar)
myvar= myvar / 6000
print(myvar)

#b=np.array([1,2,3],"Hi")
#print(b) only one type of data 
smyvar = np.array(["hi","hello"])
print(smyvar)
smyvar= smyvar +"this"
print(smyvar)

anothervar = np.zeros(600)
print(anothervar)

anothervarones = np.ones(600)
print(anothervarones)

thearry = np.array([1,6,19,30,495],dtype="f")
print(thearry)

var3 = np.array([[1,4],[5,6]])
print(var3)


#var4 = np.array([[1,4],[5]])
#print(var4)           in array all the dimentions need to be the same



var3 = np.array([[1,4,5,2,6],[2,9,2,8,4]])

print("Array Dimensions",   var3.ndim)
print("Number of rows_col", var3.shape)
print("Number of elements",var3.size    )
print("Array size", var3.nbytes,"bytes")

var4 = np.arange(1,1020,dtype="f")

print(var4)
print("Array Dimensions",   var4.ndim)
print("Number of rows_col", var4.shape)
print("Number of elements",var4.size    )
print("Array size", var4.nbytes,"bytes")

var5 = np.arange(2,100,2)
print(var5)

var6 = np.arange(1,100,2)
print(var6)

var7 = np.random.randint(1,10)
print(var7)

var8 = np.random.permutation(np.arange(1,11))
print(var8)

randomvar = np.random.rand(1,20)
print(randomvar,"\n\n\n")

randomvar = np.random.rand(3,20)
print(randomvar,"\n\n\n")

var9 = np.arange(1,17).reshape(4,4)
print(var9)
