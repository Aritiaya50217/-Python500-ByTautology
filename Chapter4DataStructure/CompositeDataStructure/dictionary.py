# Dictionary รูปแบบคือ key : value

# Create Dictionary
# key : value
dict1 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
dict2 = {"fullname" : "Artitaya Yaemjaraen","hobby" : ["coding","study"]}

print(dict1)
print("Type Dict1 :",type(dict1))
print(dict2)
print("Type Dict2 :",type(dict2))

# Read Dictionary
dict3 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
# ใช้ key ในการดึงข้อมูล (value) มาแสดง
print("Myname is",dict3["firstname"])
print("I am",dict3["age"],"years old.")


# Update Dictionary : Replace
dict4 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
# เปลี่ยน value ของ firstname เป็น Oil 
dict4["firstname"] = "Oil"
print("Firstname is :",dict4["firstname"])

# Update Dictionary : Add
# การเพิ่มข้อมูลลงไปท้ายสุด
dict5 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
# เพิ่ม 'nickname':'oil' ลงใน dictionary
dict5['nickname'] = 'oil'
print(dict5)

# Update Dictionary : update
# เพิ่มข้อมูลหลายชุด

dict6 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
dict6.update({"blood_group" : "B","height" : 160})
print("My name is",dict6["firstname"] +" "+ dict6["lastname"])
print("I am",dict3["age"],"years old.")
print("My Blood group is",dict6["blood_group"])
print("My Height is",dict6["height"],"cm.")


# Delete  Dictionary : del
dict7 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
print(dict7)
# ลบ key "lastname" 
del dict7["lastname"]
print(dict7)

# Delete Dictionary : clear
# การลบข้อมูลทั้งหมด
dict8 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
dict8.clear()
print("Result :",dict8)

# Dictionary + len
dict9 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}
print("Dictionary is Length :",len(dict9))
print("Key is Length :",len(dict9.keys()))
print("Value is Length :",len(dict9.values()))

# Dictionary + in
dict10 = {"firstname" : "Artitaya","lastname" : "Yaemjaraen","age" : 23}

# firstname เป็น key ใน dictionary หรือไม่
print("firstname key in Dictionary ?? :","firstname" in dict10.keys())
# Artitaya เป็น value ใน dictionary หรือไม่
print("Artitaya value in Dictionary ?? :","Artitaya" in dict10.values())
