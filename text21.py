#โปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชื่อ และชั้นปีทางแป้นพิมพ์แล้วแสดงข้อความต้อนรับ ดังนี้
#กรณีป้อนชั้นปี 1 แสดงข้อความ "Welcome Freshman"
#กรณีป้อนชั้นปี 2 แสดงข้อความ "Welcome Sophomore"
#กรณีป้อนชั้นปี 3 แสดงข้อความ "Welcome Junior"
#กรณีป้อนชั้นปี 4 แสดงข้อความ "Welcome Senior"
#กรณีป้อน ปีอื่นๆ  แสดงข้อความ "Oh, no ...."

print('-----------------------------------')
print('โปรแกรมแสดงความต้อนรับนักศึกษา')
print('-----------------------------------')
Student_id = input('ป้อนรหัสนักศึกษา : ')
Student_name = input('ป้อนชื่อนักศึกษา : ')
Student_year = input('ป้อนชั้นปี : ')
print('-----------------------------------')
if Student_year == '1' :
    print(f'Welcome Freshman : {Student_year} ปี')
elif Student_year == '2' :
    print(f'Welcome Sophomore : {Student_year} ปี')
elif Student_year == '3' :
    print(f'Welcome Junior : {Student_year} ปี')
elif Student_year == '4' :
    print(f'Oh, no .... : {Student_year} ปี')

print('-----------------------------------')
print('ขอบคุณที่ใช้บริการ')
print('-----------------------------------')