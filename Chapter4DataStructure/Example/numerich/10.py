''' 
เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนจริง
(float1,float2) ให้คำนวณผลบวก,ผลลบ,ผลคูณ และผลหารของจำนวนที่รับมา หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา
'''
float1 = float(input("Please Enter Number : "))
float2 = float(input("Please Enter Number : "))

print("Addition Total : ",float1 + float2)
print(type(float1 + float2))

print("Subtraction Total : ",float1 - float2)
print(type(float1 - float2))

print("Multiplication Total : ",float1 * float2)
print(type(float1 * float2))

print("Division Total : ",float1 / float2)
print(type(float1 / float2))
