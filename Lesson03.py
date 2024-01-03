
import datetime # implemented in task 2
#Task1
first_name = input("Enter your name: ")
second_name = input("Enter your surname: ")
print(f"Hello there, {first_name}, {second_name}")


#Task2
user_age = input("What age will you be this year?: ")
current_year = datetime.datetime.now().year
born_year = current_year - int(user_age)
print(f"You were born in {born_year}")

#Task3
temp_C = input("Enter current temperature in Celsius: ")
temp_F = (int(temp_C) * 9/5) + 32
print(f"You temperature in Farengate is {temp_F}")

#Task5
user_num = input("Plase enter any number: ")
if int(user_num) % 2 == 0:
    print(f"Your number {user_num} is even")
else:
    print(f"Your number {user_num} is odd")