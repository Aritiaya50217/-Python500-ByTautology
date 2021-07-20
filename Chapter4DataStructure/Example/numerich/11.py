'''
    เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นจำนวนเต็มและจำนวนจริง
    (int1,float1) ให้คำนวณผลบวก ผลลบ ผลคูณและผลหาร 
    ของจำนวนที่รับมา หลังจากนั้นให้พิมพ์ค่าและชนิดข้อมูลของทุกผลลัพธ์ออกมา
'''
int1 = int(input("Please Enter Number : "))
float1 = float(input("Please Enter Number : "))

print("Addition Total : ",int1 + float1)
print(type(int1 + float1))

print("Subtraction Total : ",int1 - float1)
print(type(int1 - float1))

print("Multiplication Total : ",int1 * float1)
print(type(int1 * float1))

print("Division Total : ",int1 / float1)
print(type(int1 / float1))