
from typing import List, Tuple, Union


def input_data() -> List[List[int]]:
    list_a_str = input("Enter list of a coeficient of integer type: ").split()
    list_a_int = [int(item) for item in list_a_str]
    list_b_str = input("Enter list of b coeficient of integer type: ").split()
    list_b_int = [int(item) for item in list_b_str]
    list_c_str = input("Enter list of c coeficient of integer type: ").split()
    list_c_int = [int(item) for item in list_c_str]
    list_a_b_c_int = [list_a_int, list_b_int, list_c_int]
    return list_a_b_c_int


def validate_input(raw_data: List[List[int]]) -> bool:
    for l in raw_data:
        if not l:
            return False

    if len(raw_data[0]) != len(raw_data[1]) != len(raw_data[2]):
        return False

    for el in raw_data[0]:
        if el == 0:
            return False

    return True




def calc_quadr(valid_data: List[List[int]]) -> List[Tuple[Union[int,str]]]:
    pass














def main():
    input_list = input_data()
    print(input_list)



if __name__ == '__main__':
    main()

