# การใช้ %d,%f,%s
# %d ใช้กับตัวเลขประเภทจำนวนเต็ม(integer)
# %f ใช้กับตัวเลขประเภททศนิยม(float)
# %s ใช้กับข้อมูลประเภทข้อความ (string)

# เอาเลข 3 มาแทนที่ตัว d

print("%d" %3)
print("%f" %6.600)
# %.2f คือ แสดงทศนิยม 2 ตัวแหน่ง
print("%.2f" %1)
print("%s" %"Hello")
print("%d %.3f %s" %(2,3.3,"Hi"))
