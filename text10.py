# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================
numbers = []

# รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
for i in range(5):
    while True:
        try:
            num = int(input(f"Enter number {i + 1} : "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
# คำนวณผลรวม
total_sum = sum(numbers)

# คำนวณค่าเฉลี่ย
average = total_sum / 5

# แสดงผลลัพธ์
print("=" * 28)
print(f"Sum of 5 numbers is : {total_sum}")
print(f"Average of 5 numbers is : {average}")
print("=" * 28)