
#Мета: Створити програму, яка приймає від користувача послідовні числа до тих пір,
# поки він не введе спеціальне значення (наприклад, stop).
# Після цього вивести середнє арифметичне введених чисел.

sum = 0
count = 0

while True:
    number = input("Введіть число (stop для завершення): ")

    if number == 'stop':
        break


    sum += float(number)
    count += 1

average = sum / count
print(f"Середнє арифметичне ваших чисел: {average}")

#pull request does not sent
#again