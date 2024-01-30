#Даний масив чисел.

#[10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

#1.1) Видалити з нього повторюючіся елементи.

#1.2) Вивести 3 найбільших числа зі зазначеного масиву.

#1.3) Вивести індекс мінімального елемента масиву.

#1.4) Вивести зазначений масив в зворотньому порядку.


list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print("Вихідний массив: ", list)


#1.1)

def duplicate(list):
    correct_list = []
    for num in list:
        if num not in correct_list:
            correct_list.append(num)
    return correct_list




#1.2)

def get_top(list):
    top_three = sorted(list, reverse=True)[:3]
    return top_three




#1.3)

def get_min_index(list):
    min_index = list.index(min(list))
    return min_index


#1.4)


def reverse_list(list):
    reversed_list = list[::-1]
    return reversed_list


def main():
    correct_list = duplicate(list)
    print("Масив без дублікатів: ", correct_list)

    reversed_list = reverse_list(correct_list)
    print("Перевернутий масив: ", reversed_list)

    min_index = get_min_index(reversed_list)
    print("Індекс найменшого числа: ", min_index)

    top_three = get_top(reversed_list)
    print("Топ три значення: ", top_three)


if __name__ == '__main__':
    main()