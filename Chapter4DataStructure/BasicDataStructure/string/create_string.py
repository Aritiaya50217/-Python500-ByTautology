# create string
char1 = "Hello World"
char2 = "123456789"
print(char1)
print(type(char1))

# Read string
char3 = "12345"
# การเข้าถึงอักขระแต่ละตัวจะเข้าถึงผ่าน index(ลำดับ)
# แสดงข้อมูลลำดับที่ 0
# result = 1
print(char3[0])
# result = 4
print(char3[3])
# char3[-1] นับจากตัวหลังสุด
# result = 5
print(char3[-1])

char4 = "12345678910"
# รูปแบบ [start:stop:step]
# อ่านตั้งแต่ index 3 จนถึงสุดท้าย
print(char4[3:])
# อ่านตั้งแต่ index 0 - 6
print(char4[:7])
# อ่านตั้งแต่ index 3 - 6
print(char4[3:7])

# String + replace 
char5 = "abc"
# แทนที่ตัวอักษร a เป็น A 
print(char5.replace("a","A"))
print(char5.replace("bc","DE"))

# String + len
# นับความยาว,จำนวน ของข้อมูลภายใน
char6 = "12345"
print(len(char6))

# String + in
char7 = "Python"
# P อยู่ใน char7 หรือไม่
print("P" in char7)

# String + split (การตัดคำ)
char8 = "one-two-three" 
# ตัดเครื่องหมาย '-' ออกจากข้อความ
print(char8.split('-'))

char9 = "I love coding"
# แยกออกที่เป็นคำ 
# result = ['I', 'love', 'coding']
print(char9.split(' '))

# String + Concatenation
# การเอาข้อความมาต่อกัน
char10 = "ab"
char11 = "cd"
char12 = "12"
char13 = "34"
print(char10 + char11 + char12 + char13)