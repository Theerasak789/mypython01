fullname = input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print("-----------------------------")
print(f'สวัสดีคุณ {fullname}')
print(f'คุณเกิดในปี พ.ศ. {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}')
print("-----------------------------") 
# ใช้ ,
print("สวัสดีคุณ", fullname)
print("คุณเกิดในปี พ.ศ.", year_born, "ตอนนี้คุณอายุ", 2568 - int(year_born))
print("-----------------------------") 
# ใช้ +
print("สวัสดีคุณ " + fullname)
print("คุณเกิดในปี พ.ศ. " + year_born + " ตอนนี้คุณอายุ " + str(2568 - int(year_born)))
print("-----------------------------") 
# ใช้format
print("สวัสดีคุณ {}".format(fullname))
print("คุณเกิดในปี พ.ศ. {} ตอนนี้คุณอายุ {}".format(year_born, 2568 - int(year_born)))
print("-----------------------------")