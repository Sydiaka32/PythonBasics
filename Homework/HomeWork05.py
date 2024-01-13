from typing import List

#1 Свторіть функцію, яка приймає список чисел і повертає список їх квадратів

def get_user_input() -> List[str]:
    input_str = input("Input list of numbers devided by space: ")
    return input_str.split(" ")

def validate_list(input_list: List[str]) -> List[int]:
    try:
        valid_list = [int(el) for el in input_list]
        return valid_list
    except ValueError as err:
        print(err)
        raise TypeError("Please enter only numbers")

def squared_list(valid_list: List[int]) -> List[int]:
    result = [num ** 2 for num in valid_list]
    return result



def main():
    user_input = get_user_input()
    valid_list = validate_list(user_input)
    result = squared_list(valid_list)
    print(result)



if __name__ == '__main__':
    main()

