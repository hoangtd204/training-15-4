number = int(input("Nhập một số nguyên dương: "))

def check_OddNumber(number):
    sum = 0
    while number > 0:
        lastNumber = number % 10
        if lastNumber % 2 == 1:
            sum += lastNumber
        number = number // 10
    return sum

# Gọi hàm và in kết quả
print("Tổng các chữ số lẻ là:", check_OddNumber(number))
