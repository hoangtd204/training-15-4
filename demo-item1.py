#variable
myScore = {'Physics': 8, 'Math': 8}

#function
def check_OddNumberByWhile():
    number = int(input("Nhập một số nguyên dương: "))
    sum = 0
    while number > 0:
        lastNumber = number % 10
        if lastNumber % 2 == 1:
            sum += lastNumber
        number = number // 10
    print(f"Tổng các chữ số lẻ là {sum}")

def checkScore(myScore):
    for score in myScore:
        print(score, myScore[score])

#call function
def main():
    while True:
        print("Chọn phần kiểm tra") 
        print("1. Bài for")
        print("2. Bài while")
        print("3. Thoát")
        choice = input("👉 Chọn: ")

        if choice == '1':
            checkScore(myScore)
        elif choice == '2':
            check_OddNumberByWhile()
        elif choice == '3':
            break
        else:
            print(" Lựa chọn không hợp lệ.")

main()
