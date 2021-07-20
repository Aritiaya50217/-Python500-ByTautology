'''
เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนเต็ม (int1,int2)
ให้คำนวณผลบวก,ผลลบ,ผลคูณ และผลหารของจำนวนที่รับมา 
หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา
'''

int1 = int(input("First Number: "))
int2 = int(input("Second Number: "))

print("Addition Total : ",int1 + int2)
print(type(int1 + int2))

print("Subtraction Total : ",int1 - int2)
print(type(int1 - int2))

print("Multiplication Total : ",int1 * int2)
print(type(int1 * int2))

print("Division Total : ",int1 / int2)
print(type(int1 / int2))

# แบบที่ 2
a = int1 + int2
b = int1 - int2
c = int1 * int2
d = int1 / int2
print("-------------------------------")
print("วิธีที่ 2")
print("ผลบวก %s" %a,type(a))
print("ผลลบ %s" %b,type(b))
print("ผลคูณ %s" %c,type(c))
print("ผลหาร %s" %d,type(d))
