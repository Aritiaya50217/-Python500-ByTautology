# CRUD + sort + len + in
# create list
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d"]
list3 = [1,2,3,"a","b","c"]

print(list3)
print(type(list3))

# Read list
list4 = [1,2,3,4,"a","b","c"]
print(list4[:6])

# Update list : replace
list5 = [1,2,3,5]
print(list5)
# เปลี่ยนตัวแหน่งสุดท้ายเป็นเลข 6
list5[-1] = 6
print(list5)
list5[2] = 4
print(list5)

# Update list : append (การนำข้อมูลใหม่มาต่อท้าย)
list6 = [1,2,3,"a","b","c"]
# เพิ่ม e ลงใน list6
list6.append("e")
print(list6)

# Update List : extend (การนำ list มาต่อกัน)
list7 = [1,2,3]
list8 = [4,5,6]
# list7 เป็น list แรก แล้วนำ list8 มาต่อท้าย
list7.extend(list8)
print(list7)

# Update List : insert (การแทรกข้อมูล)
list9 = [1,2,3]
# 1 คือ index 
# "one" คือ ข้อมูลที่เราต้องการนำไปแทรกใน list
# insert(1,"one") = แทรกคำว่า one ลงในตำแหน่งที่ 1
list9.insert(1,"one")
print(list9)

# Delete List : del
list11 = [1,2,3,4,5]
print(list11)
# ลบตำแหน่งที่ 2 ใน list
del list11[2]
print(list11)
# ลบตำแหน่งที่ -2 ใน list
del list11[-2]
print(list11)

# Delete List : remove (การลบโดยระบุค่าข้อมูลที่ต้องการ)
list12 = [1,2,3,4]
# ลบ 1 ออกจาก list
list12.remove(1)
# result = [2, 3, 4]
print(list12)

# Delete List : clear (ลบข้อมูลทุกตัวใน list)
list13 = [1,2,3,4,5]
list13.clear()
# result = []
print(list13)

# List + sort 
# การเรียงลำดับจากน้อยไปมาก
list14 = [6,2,3,4]
list14.sort()
print(list14)
# เรียงจากมากไปน้อย
# reverse=True ใส่ True เสมอ ถ้าใส่ False จะเรียงน้อยไปมาก
list14.sort(reverse=True)
print(list14)

# การใช้ sorted 
# เป็นการเรียงลำดับแล้ว สร้างเป็นตัวแปรใหม่ขึ้นมา
sorted_list14 = sorted(list14)
print(sorted_list14)

# เรียงลำดับจากมากไปน้อย
sorted_list14 = sorted(list14,reverse=True)
print(sorted_list14)

# List + len การนับจำนวน
list15 = [1,1,1,1,1,1]
print(len(list15))

# List + in (ตรวจสอบว่า ... มีใน list หรือไม่)
list16 = [1,5,6,7,8]
# มีเลข 1 ใน list หรือไม่
print(1 in list16)
