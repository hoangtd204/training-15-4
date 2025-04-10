import json
import os


def read_user_from_file(filename):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            return json.load(f)
    return []


def get_user_input():
    name = input("Vui lòng nhập tên: ")
    age = int(input("Vui lòng nhập tuổi: "))
    skills = input("Nhập kĩ năng (phân tách bằng dấu phẩy): ")

    user = {
        "name": name,
        "age": age,
        "skill": [skill.strip() for skill in skills.split(",")],
    }
    return user


def save_user_to_file(filename, users):
    with open(filename, "w") as f:
        json.dump(users, f, indent=4)


def main():
    filename = "users.json"
    users = read_user_from_file(filename)

    while True:
        user = get_user_input()
        users.append(user)

        conti = input("Bạn có muốn nhập tiếp không (y/n)? ")
        if conti.lower() != "y":
            break

    save_user_to_file(filename, users)


main()
