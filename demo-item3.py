import json
import os

# Kiểm tra xem file đã có data bên trong chưa
users = []

if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
    with open('users.json', 'r') as f:
        users = json.load(f)

# Nhập người dùng mới
while True:
    name = input("Nhập tên: ")
    age = int(input("Nhập tuổi: "))
    skills = input("Nhập kỹ năng (phân cách bởi dấu phẩy): ").split(',')

    user = {
        "name": name,
        "age": age,
        "skills": [skill.strip() for skill in skills]
    }
 # Thêm vào danh sách đã có
    users.append(user) 

    tiep = input("Nhập thêm người nữa? (y/n): ")
    if tiep.lower() != 'y':
        break

#Ghi toàn bộ danh sách người dùng vào file 
with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)