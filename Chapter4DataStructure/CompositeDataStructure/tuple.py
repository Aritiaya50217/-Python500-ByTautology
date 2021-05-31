# Tuple คล้ายกับ list แต่ไม่สามารถแก้ไขได้

# Create Tuple
tuple1 = (1,2,3,4)
tuple2 = ("a","b","c","d")
tuple3 = (1,2,3,4,5,"a") 

print(tuple1)
print("Type Tuple1 :",type(tuple1))
print(tuple2)
print("Type Tuple2 :",type(tuple2))
print(tuple3)
print("Type Tuple3 :",type(tuple3))

# Read Tuple
tuple4 = (1,2,3,4,"a","c")
print(tuple4[0])
print(tuple4[-1])

# Tuple + len
tuple5 = (1,2,3,'a','b')
print(len(tuple5))

#Tuple + in
tuple6 = (1,1,1,1,9)
print(1 in tuple6)
