print('**********************')
print('ยินดีต้อนรับเข้าสู่โปรแกรมคํานวณ')
print('**********************')

import math
while True:
    print('\n====== เมนู =======')
    print('1. พื่นที่สี่เหลี่ยม')
    print('2. พื้นที่่วงกลม')
    print('3. ปริมาตรทรงสี่เหลี่ยม')
    print('4. ปริมาตรทรงกลม')
    print('0. ออกจากการทำงาน')
    choice = int(input('กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0: '))

    if choice == 1:
       w = float(input('ป้อนความกว้าง : '))
       h = float(input('ป้อนความยาว : '))
       area = w * h
       print(f'พื้นที่สี่เหลี่ยม = : {area:.2f}')
       print('***********************')
    elif choice == 2:
       r = float(input('ป้อนรัศมี : '))
       area = math.pi * r * r
       print(f'พื้นที่วงกลม = : {area:.2f}')
       print('*************************')
    elif choice == 3:
       w = float(input('ป้อนความกว้าง : '))
       l = float(input('ป้อนความยาว : '))
       h = float(input('ป้อนความสูง : '))
       volume = w * l * h
       print(f'ปริมาตรทรงสี่เหลี่ยม = : {volume:.2f}')
       print('*************************')
    elif choice == 4:
       r = float(input('ป้อนรัศมี : '))
       volume = (4/3) * math.pi * r * r
       print(f'ปริมาตรทรงกลม = : {volume:.2f}')
       print('*************************')
    elif choice == 0:
       print('จบการทำงาน')
       print('*************************')
       break
    else:
         print('กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น')