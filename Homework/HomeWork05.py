from typing import List

#1 Свторіть функцію, яка приймає список чисел і повертає список їх квадратів

def get_user_input() -> List[str]:
    input_str = input("Input list of numbers divided by space: ")
    return input_str.split(" ")

def validate_list(input_list: List[str]) -> List[int]:
    valid_list = []

    for el in input_list:
        if not el.strip():
            raise TypeError("Empty input detected. Please enter valid numbers.")

        try:
            num = int(el)
            valid_list.append(num)
        except ValueError as err:
            print(f"Invalid input for element '{el}': {err}")
            raise TypeError("Invalid input detected. Please enter only numbers")

    return valid_list


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

