#variable
number = int(input("Nhập một số nguyên dương: "))
myScore= {'Physics':8,'Math':8}

#function
def check_OddNumberByWhile(number):
    sum = 0
    while number > 0:
        lastNumber = number % 10
        if lastNumber % 2 == 1:
            sum += lastNumber
        number = number // 10
    return sum

def checkScore(myScore):
    for score in myScore:
      print(score,myScore[score])

#call function
print("Tổng các chữ số lẻ là:", check_OddNumberByWhile(number))

checkScore(myScore)