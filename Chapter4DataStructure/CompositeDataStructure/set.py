# Set เป็นการเก็บข้อมูลที่ไม่สามารถอ้างอิงถึงสมาชิกที่อยู่ด้านในแบบเฉพาะเจาะจงได้
# ไม่มี index
# ไม่มี key : value
# มี Union,Intersection,Difference,Symmetric Difference

# Create Set
set1 = {1,2,3,4}
set2 = {2,3,4,5,6}
print(set1)
print("Set1 Type:",type(set1))
print(set2)
print("Set2 Type:",type(set2))

# Read Set
# ต้องใช้ for loop ในการอ่านค่าสมาชิก
# set จะไม่มีการเรียงลำดับ
set3 = {'a','b','c','d','e'}
for x in set3 :
    print(x)

# Update Set: add
set4 = {'a','b','c','d','e'}
# เพิ่ม 1 เข้าไปใน set โดยที่ไม่มีการระบุตำแหน่ง 1 จะถูกเก็บไว้ในตำแหน่งใดก็ได้
set4.add(1)
print(set4)

# Update Set : update
#  เพิ่มข้อมูลลงใน set แบบหลายค่า
set5 = {'a','b','c','d','e'}
set5.update({1,2})
print(set5)

# Update Set : remove
# การลบสมาชิกแบบระบุค่า
set6 = {'a','b','c','d','e'}
# ลบ a ออกจาก set
set6.remove('a')
print(set6)

# Delete Set: clear
# ลบข้อมูลทั้งหมดใน set
set7 = {'a','b','c','d','e'}
set7.clear()
print("After Delete Set :",set7)

# Set + len (การนับความยาวข้อมูล)
set8 ={'a','b','c','d','e'}
print("Set is Length :",len(set8))

# Set + Union
# การเอาข้อความที่ซ้ำกัน ออกมาแค่ค่าเดียว
setA = {1,2,3,4,5}
setB = {3,4,5,6,7,8}
print("SetA Union SetB :",setA | setB)

# Set + Intersection
# สมาชิกที่มีร่วมกัน
setC = {1,2,3,4,5}
setD = {3,4,5,6,7,8}
print(setC & setD)

# Set + Difference
setE = {1,2,3,4,5}
setF = {3,4,5,6,7}
# สมาชิกที่มีใน E แต่ ไม่มีใน F
print(setE - setF) 
# สมาชิกที่มีใน F แต่ ไม่มีใน E
print(setF - setE) 


# Set + Symmetric Difference
''' (setG ∪ setH) - (setG ∩ setH)
สมาชิกของทั้ง 2 set - สมาชิกที่มีในทั้ง 2 set
''' 
setG = {1,2,3,4,5}
setH = {3,4,5,6,7}
print(setG ^ setH) # output {1, 2, 6, 7}
