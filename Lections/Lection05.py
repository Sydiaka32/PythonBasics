

from typing import List



def get_user_input() -> List[str]:
    """
    :return: list of string from terminal
    """
    input_string = input("Input list of numbers divided be space: ")
    return input_string.split(" ")


def validate_list(raw_list: List[str]) -> List[int]:
    try:
        result_list = [int(el) for el in raw_list]
        return result_list
    except ValueError as err:
        print(err)
        raise TypeError("Letters insted numbers")


def get_sum_list(my_list: List[int]) -> int:
    """
    :param my_list: valid list of int
    :return: sum of list
    """
    result = 0
    for el in my_list:
        result += el
    return result


def main():
    user_input = get_user_input()
    valid_list = validate_list(user_input)
    result = get_sum_list(valid_list)
    print(result)



if __name__ == '__main__':
    main()