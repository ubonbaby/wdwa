# YOUR CODE HEREimport pandas as pd

# อ่านข้อมูลจากไฟล์ CSV
data = pd.read_csv('data.csv')

# กรองข้อมูลที่อายุมากกว่า 40 ปี
data_filtered = data[data['Age'] > 40]

# นับจำนวนผู้ชาย (male) แยกตาม Pclass
male_counts = data_filtered[data_filtered['Sex'] == 'male']['Pclass'].value_counts()
# นับจำนวนผู้หญิง (female) แยกตาม Pclass
female_counts = data_filtered[data_filtered['Sex'] == 'female']['Pclass'].value_counts()

# แสดงผลสำหรับ male (age > 40)
print("male (age>40)")
for i in range(1, 4):
    print(f"Pclass {i}: {male_counts.get(i, 0)}")

# แสดงผลสำหรับ female (age > 40)
print("female (age>40)")
for i in range(1, 4):
    print(f"Pclass {i}: {female_counts.get(i, 0)}")
